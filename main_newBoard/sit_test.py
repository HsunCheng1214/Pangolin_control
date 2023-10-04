import os, sys, math
import numpy as np
# import cv2
import threading
# import pygame
import time
import ServoCmd 
from time import sleep

deviation = [0 ,-100, 100, 100]
# sleep(10)


ServoCmd.setServoPulse(9, 1500 + deviation[2], 1000)
ServoCmd.setServoPulse(10, 1500 + deviation[3], 1000)
ServoCmd.setServoPulse(6, 1500 + deviation[0], 1000)
ServoCmd.setServoPulse(8, 1500 + deviation[1], 1000)
sleep(1)

ServoCmd.setServoPulse(9, 2300 + deviation[2], 300)
ServoCmd.setServoPulse(10, 700 + deviation[3], 300)
ServoCmd.setServoPulse(6, 500 + deviation[0], 300)
ServoCmd.setServoPulse(8, 2500 + deviation[1], 300)
sleep(0.3)

ServoCmd.setServoPulse(9, 2000 + deviation[2], 150)
ServoCmd.setServoPulse(10, 1000 + deviation[3], 150)
ServoCmd.setServoPulse(6, 2000 + deviation[0], 150)
ServoCmd.setServoPulse(8, 1000 + deviation[1], 150)
sleep(0.15)

ServoCmd.setServoPulse(9, 1600 + deviation[2], 1000)
ServoCmd.setServoPulse(10, 1400 + deviation[3], 1000)
ServoCmd.setServoPulse(6, 2000 + deviation[0], 1000)
ServoCmd.setServoPulse(8, 1000 + deviation[1], 1000)
sleep(3)



ServoCmd.setServoPulse(9, 1600 + deviation[2], 1000)
ServoCmd.setServoPulse(10, 1400 + deviation[3], 1000)
ServoCmd.setServoPulse(6, 1500 + deviation[0], 1000)
ServoCmd.setServoPulse(8, 1500 + deviation[1], 1000)
sleep(1)

ServoCmd.setServoPulse(9, 2200 + deviation[2], 1000)
ServoCmd.setServoPulse(10, 800 + deviation[3], 1000)
ServoCmd.setServoPulse(6, 1500 + deviation[0], 1000)
ServoCmd.setServoPulse(8, 1500 + deviation[1], 1000)
sleep(1)
ServoCmd.setServoPulse(9, 1500 + deviation[2], 1000)
ServoCmd.setServoPulse(10, 1500 + deviation[3], 1000)
ServoCmd.setServoPulse(6, 1500 + deviation[0], 1000)
ServoCmd.setServoPulse(8, 1500 + deviation[1], 1000)
sleep(1)
# ServoCmd.setServoPulse(9, 2000 + deviation[2], 150)
# ServoCmd.setServoPulse(10, 1000 + deviation[3], 150)
# ServoCmd.setServoPulse(6, 2000 + deviation[0], 150)
# ServoCmd.setServoPulse(8, 1000 + deviation[1], 150)
# sleep(0.15)

# ServoCmd.setServoPulse(9, 1600 + deviation[2], 3000)
# ServoCmd.setServoPulse(10, 1400 + deviation[3], 3000)
# ServoCmd.setServoPulse(6, 2000 + deviation[0], 3000)
# ServoCmd.setServoPulse(8, 1000 + deviation[1], 3000)
# sleep(3)