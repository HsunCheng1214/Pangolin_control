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
import argparse
import itertools
import json
import zenoh
from zenoh import config
from multi_robot_datatype import BatteryState, OverViewState, JointStates, UWBState, Vector3, Twist


# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='z_pub',
    description='zenoh pub example')
parser.add_argument('--mode', '-m', dest='mode',
                    choices=['peer', 'client'],
                    type=str,
                    help='The zenoh session mode.')
parser.add_argument('--connect', '-e', dest='connect',
                    metavar='ENDPOINT',
                    action='append',
                    type=str,
                    help='Endpoints to connect to.')
parser.add_argument('--listen', '-l', dest='listen',
                    metavar='ENDPOINT',
                    action='append',
                    type=str,
                    help='Endpoints to listen on.')
parser.add_argument('--key', '-k', dest='key',
                    default='pangolin0/cmd_vel',
                    type=str,
                    help='The key expression to publish onto.')
parser.add_argument('--value', '-v', dest='value',
                    default='Pub from Python!',
                    type=str,
                    help='The value to publish.')
parser.add_argument("--iter", dest="iter", type=int,
                    help="How many puts to perform")
parser.add_argument('--config', '-c', dest='config',
                    metavar='FILE',
                    type=str,
                    help='A configuration file.')
parser.add_argument('-d', '--delay', type=float, default=0.05, help='delay between each frame in seconds')

args = parser.parse_args()
conf = zenoh.Config.from_file(args.config) if args.config is not None else zenoh.Config()
if args.mode is not None:
    conf.insert_json5(zenoh.config.MODE_KEY, json.dumps(args.mode))
if args.connect is not None:
    conf.insert_json5(zenoh.config.CONNECT_KEY, json.dumps(args.connect))
if args.listen is not None:
    conf.insert_json5(zenoh.config.LISTEN_KEY, json.dumps(args.listen))
key = args.key
value = args.value

# initiate logging
zenoh.init_logger()

print("Opening session...")
session = zenoh.open(conf)

print(f"Declaring Publisher on '{key}'...")
pub = session.declare_publisher(key)

while True:
    time.sleep(0.5)
    # linear = [0.0, 0.0, 0.0]
    # angular = [0.0, 0.0, 1.0]
    cmd = Twist(linear= Vector3(x=0.0, y=0.0, z=0.0),
                    angular=Vector3(x=0.0, y=0.0, z=1.0))
    print(f"Putting Data ('{key}': '{cmd}')...")
    pub.put(cmd.serialize())

pub.undeclare()
session.close()
