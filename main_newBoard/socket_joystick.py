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


class SocketClient():

    def __init__(self, addr, port):

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
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # self.server_socket.bind()
                # self.server_socket.connect((self.server_address, self.server_port))
                self.server_socket.listen(1)
                print("Successful Connect to joystick")
                self.connection_success = True
                self.process_thread = threading.Thread(target=self.processData, daemon=True)
                self.process_thread.start()
            except ConnectionRefusedError:
                self.connection_success = False
    
    def processData(self):
        while not self.force_quit:
            msg_data = self.server_socket.recv(8192).decode('utf-8')
            # if len(msg_data) < self.DEFAULT_LEN:
            #     # self.decodeData(msg_data)
            print(msg_data)
    
    # def decodeData(self, msg_data):
    #     server_data = pickle.loads(msg_data)
    #     print("ID {} L_cmd {} A_cmd {} ".format(server_data.ID, server_data.Linear, server_data.Angular))
    #     self.server_cmd = server_data

    def getCMDInfo(self):
        return self.server_cmd
    
    def closeSocketServer(self):
        self.force_quit = True
        self.server_socket.close()
        # self.robot_manager.closeStatusManager()

if __name__ == "__main__":

    server_ip = "0.0.0.0"
    server_port = 8000
    manager = SocketClient(server_ip, server_port)
    
    # while True:
    #     manager.connectToServer()

    while True:
        try:
            cmd = input("CMD: ")
            if cmd == "q":
                break
        except Exception as e:
            traceback.print_exc()
            break
    manager.closeSocketServer()
    # manager.closeStatusManager()