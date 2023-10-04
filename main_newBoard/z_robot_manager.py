import argparse
import curses
import zenoh
import json
from dataclasses import dataclass
from datetime import datetime
from pycdr2 import IdlStruct
from pycdr2.types import int8, int32, uint32, uint8, float64, float32, sequence, array
from typing import List
import threading
import traceback
import time
from multi_robot_datatype import BatteryState, OverViewState, JointStates, UWBState, Vector3, Twist
import socket
import numpy as np
import pickle

class RobotPickle():
    def __init__(self, id ,linear, angular):
        self.ID = id
        self.Linear = linear
        self.Angular = angular

class SocketClient():

    def __init__(self, addr, port):

        self.robot_manager = RobotStatusManager(robot_num=1)
        # self.robot_manager.activeStatusManager()

        self.server_address = addr
        self.server_port = port
        self.connection_success = False
        self.DEFAULT_LEN = 100
        self.force_quit = False
        self.process_thread = threading.Thread()

        self.server_cmd = None
        self.connectToServer()
    
    def connectToServer(self):
        if not self.connection_success:
            try:
                self.unity_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.unity_socket.connect((self.server_address, self.server_port))
                print("Successful Connect to Unity Server")
                self.connection_success = True
                self.process_thread = threading.Thread(target=self.processData, daemon=True)
                self.process_thread.start()
            except ConnectionRefusedError:
                self.connection_success = False
    
    def processData(self):
        while not self.force_quit:
            msg_data = self.unity_socket.recv(2048)
            if len(msg_data) < self.DEFAULT_LEN:
                self.decodeData(msg_data)
                self.robot_manager.sendRobotCMD(self.server_cmd)
    
    def decodeData(self, msg_data):
        server_data = pickle.loads(msg_data)
        print("ID {} L_cmd {} A_cmd {} ".format(server_data.ID, server_data.Linear, server_data.Angular))
        self.server_cmd = server_data

    def getCMDInfo(self):
        return self.server_cmd
    
    def closeSocketServer(self):
        self.force_quit = True
        self.unity_socket.close()
        self.robot_manager.closeStatusManager()

class PangolinState():

    def __init__(self, id, zenoh_config):
        
        self.id = str(id)
        self.input_prefix = 'pangolin' + self.id

        self.battery_state = None
        self.joint_state = None
        self.battery_state_sub_ = None
        self.joint_state_sub_ = None

        self.zenoh_session = zenoh.open(zenoh_config)
        # self.createTopicSub()
    
    def pubTwistCMD(self, linear_cmd, angular_cmd):
        cmd_topic = self.input_prefix + '/cmd_vel'
        print(cmd_topic)
        cmd = Twist(linear= Vector3(x=linear_cmd, y=0.0, z=0.0),
                    angular=Vector3(x=0.0, y=0.0, z=angular_cmd))
        self.zenoh_session.put(cmd_topic, cmd.serialize())
        
    def closeConnect(self):
        if self.battery_state_sub_ is not None:
            self.battery_state_sub_.undeclare()
        if self.joint_state_sub_ is not None:
            self.joint_state_sub_.undeclare()



class RobotStatusManager():
    
    def __init__(self, robot_num = 1):  

        """ private definition """
        self.zenoh_config_ = None
        self.zenoh_session_ = None
        self.battery_state_sub_ = None
        self.joint_state_sub_ = None
        self.update_thread_enable_ = False

        self.robot_id = None

        self.turtlebot_list = list()
        self.pangolin_list = list()
        self.MAX_ROBOT_NUM = robot_num

        # self.input_prefix_ = 'rt' #default setting

        self.output_prefix_ = 'turtlebot'

        """ public definition """

        self.zenohInit()
        


    def setArgParser(self) -> argparse.ArgumentParser:
        arg_parser = argparse.ArgumentParser(prog='robot-manager',
                                                description='zenoh robot manager')
        arg_parser.add_argument('-e', '--connect', type=str, metavar='ENDPOINT', action='append')
        arg_parser.add_argument('-l', '--listen', type=str, metavar='ENDPOINT', action='append')
        arg_parser.add_argument('-d', '--delay', type=float, default=0.05, help='delay between each frame in seconds')
        arg_parser.add_argument('-m', '--mode', type=str, default='client')
        arg_parser.add_argument('-c', '--config', type=str, metavar='FILE')

        return arg_parser
        
        
    
    def zenohInit(self):
        zenoh_arg = self.setArgParser().parse_args()
        self.zenoh_config_ = zenoh.config_from_file(zenoh_arg.config) if zenoh_arg.config is not None else zenoh.Config()
        if zenoh_arg.mode is not None:
            self.zenoh_config_.insert_json5(zenoh.config.MODE_KEY, json.dumps(zenoh_arg.mode))
        if zenoh_arg.connect is not None:
            self.zenoh_config_.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(zenoh_arg.connect))
        if zenoh_arg.listen is not None:
            self.zenoh_config_.insert_json5(zenoh.config.LISTEN_KEY, json.dumps(zenoh_arg.listen))

        self.zenoh_session_ = zenoh.open(self.zenoh_config_)

        self.initRobotCommunication()
        
    def initRobotCommunication(self):
        for id in range(self.MAX_ROBOT_NUM):
            # turlebot_state = TurtlebotState(id, zenoh_config= self.zenoh_config_)
            # self.turtlebot_list.append(turlebot_state)
            pangolin_state = PangolinState(id, zenoh_config= self.zenoh_config_)
            self.pangolin_list.append(pangolin_state)
        print("Init Robot State Successful")
    
    def sendRobotCMD(self, cmd):
        if cmd is not None:
            print("cmd                      ID {} linear {} angular {}".format(cmd.ID, cmd.Linear, cmd.Angular))
            if cmd.ID < self.MAX_ROBOT_NUM:
                self.pangolin_list[cmd.ID].pubTwistCMD(cmd.Linear, cmd.Angular)
        else:
            for id in range(self.MAX_ROBOT_NUM):
                self.pangolin_list[id].pubTwistCMD(0, 0)


    def closeStatusManager(self):
        if self.update_thread_enable_:
            self.update_thread_enable_ = False
        if self.is_uwb_master:
            self.uwb_system.closeSystem()
        self.zenoh_session_.close()


if __name__ == "__main__":

    server_ip = "192.168.100.65"
    server_port = 8000
    manager = SocketClient(server_ip, server_port)

    while True:
        try:
            cmd = input("CMD: ")
            if cmd == "q":
                break
        except Exception as e:
            traceback.print_exc()
            break
    manager.closeSocketServer()
    manager.closeStatusManager()