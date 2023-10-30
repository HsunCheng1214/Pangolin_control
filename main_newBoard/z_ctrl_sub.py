#
# Copyright (c) 2022 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#

import sys
import time
from datetime import datetime
import argparse
import json
import zenoh
from zenoh import Reliability, Sample
from multi_robot_datatype import BatteryState, OverViewState, JointStates, UWBState, Vector3, Twist
import ServoCmd 
import threading
from queue import Queue

class PangolinStatus():
    
    def __init__(self):
        self.arg_parser_ = argparse.ArgumentParser(prog='zenoh-test', description='zenoh test launcher')
        self.arg_parser_.add_argument('-e', '--connect', type=str, metavar='ENDPOINT', action='append')
        self.arg_parser_.add_argument('-m', '--mode', type=str, default='client')
        self.arg_parser_.add_argument('-l', '--listen', type=str, metavar='ENDPOINT', action='append')
        self.arg_parser_.add_argument('-c', '--config', type=str, metavar='FILE')
        self.arg_parser_.add_argument('-d', '--delay', type=float, default=0.05, help='delay between each frame in seconds')
        self.arg_parser_.add_argument('--key', '-k', dest='key', default='pangolin0/cmd_vel', type=str, help='The key expression to subscribe to.')
        
        self.key_ = None
        self.zenoh_config_ = None
        self.zenoh_session_ = None
        self.twist = None
        self.zenohInit()
        
        self.q = Queue()
        threads = []
        threads.append(threading.Thread(target = self.control_thread, args = (self.q, )))
        threads[0].start()
        
    def zenohInit(self):
        zenoh_arg = self.arg_parser_.parse_args()
        self.zenoh_config_ = zenoh.config_from_file(zenoh_arg.config) if zenoh_arg.config is not None else zenoh.Config()
        if zenoh_arg.mode is not None:
            self.zenoh_config_.insert_json5(zenoh.config.MODE_KEY, json.dumps(zenoh_arg.mode))
        if zenoh_arg.connect is not None:
            self.zenoh_config_.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(zenoh_arg.connect))
        if zenoh_arg.listen is not None:
            self.zenoh_config_.insert_json5(zenoh.config.LISTEN_KEY, json.dumps(zenoh_arg.listen))
        self.key_ = zenoh_arg.key


    def subPangolinStatus(self, sample: Sample):
        
        self.twist = Twist.deserialize(sample.payload)
        print(f"linear: {self.twist.linear}, angular: {self.twist.angular}")
        self.q.put(self.twist)
        # ServoCmd.move(linear=self.twist.linear, angular=self.twist.angular)


    def activeTestLauncher(self):
            zenoh.init_logger()
            print("Initial Zenoh...")
            self.zenoh_session_ = zenoh.open(self.zenoh_config_)
            self.overview_state_sub_ = self.zenoh_session_.declare_subscriber(self.key_, self.subPangolinStatus)


    def closeStatusManager(self):
        self.overview_state_sub_.undeclare()
        self.zenoh_session_.close()

    def control_thread(self, queue_data):
            while True:
                # print("1")
                if queue_data != None:
                    cmd_vel = queue_data.get()
                    queue_data.queue.clear()
                if cmd_vel != None and self.twist.linear != 0.0 and self.twist.angular !=0.0:
                    # print("1")
                    if self.twist.linear == -0.0:
                        # print(f"ctrl :     {cmd_vel}")
                        ServoCmd.move(linear=self.twist.linear, angular=self.twist.angular)
                        # ServoCmd.move(linear=self.twist.angular, angular=self.twist.linear)
                    else:
                        
                        ServoCmd.move(linear=self.twist.linear, angular=self.twist.angular)
        


if __name__ == "__main__":

    pangolin_status = PangolinStatus()
    pangolin_status.activeTestLauncher()

    c = '\0'
    while c != 'q':
        c = sys.stdin.read(1)
        if c == '':
            #print("1")
            time.sleep(0.1)

    pangolin_status.closeStatusManager()
