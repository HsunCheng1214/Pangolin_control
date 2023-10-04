# from gpiozero import AngularServo
from time import sleep
import ServoCmd


def forward(servo_angle:list, sleepTime=1.0):
     ServoCmd.setServoPulse(2, servo_angle[0]*6.25+1500, 250)
     ServoCmd.setServoPulse(4, servo_angle[1]*6.25+1500, 250)
     ServoCmd.setServoPulse(6, servo_angle[2]*6.25+1500, 250)
     ServoCmd.setServoPulse(8, servo_angle[3]*6.25+1500, 250)
     sleep(sleepTime)

try:
     servo_angle = [40, 40, -40, -40] 
     forward(servo_angle, 1)

     while True:
          servo_angle = [20, 3, 3, -20] 
          forward(servo_angle, 0.25)

          servo_angle = [-38, 3, 3, 38] 
          forward(servo_angle, 0.25)

          servo_angle = [-40, -40, 40, 40] 
          forward(servo_angle, 0.25)

          servo_angle = [0, -20, 20, 0] 
          forward(servo_angle, 0.25)


          servo_angle = [0, 38, -38, 0] 
          forward(servo_angle, 0.25)

          servo_angle = [40, 40, -40, -40] 
          forward(servo_angle, 0.25)

except KeyboardInterrupt:
	print("Program stopped")