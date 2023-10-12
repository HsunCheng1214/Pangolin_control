#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time 

pin = input("pin: ")

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(pin), GPIO.IN, GPIO.PUD_UP)

while True:
    time.sleep(0.05)
    if GPIO.input(int(pin)) == 0:
        print("button press !!!")
        while GPIO.input(int(pin)) == 0:
            time.sleep(0.01)