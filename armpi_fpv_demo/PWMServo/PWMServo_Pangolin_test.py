from time import sleep
import threading
from Board import setPWMServoPulse
import sys
# sys.path.append('/home/ubuntu/ArmPi/HiwonderSDK/PWMServo')
print("Pangolin feet test ~~~~~~~")

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
#-----------------------------------------------------------------------------------------

# old version ~~~~~~~~~~
# def forward(servo_angle=[40, 40, -40, -40] , sleepTime=1.0, servo_rate=[1.0, 1.0]):
#     deviation = [-100 ,0, 40, 120]
#     setServoPulse(9, servo_rate[0]*servo_angle[0]*6.25+1500 + deviation[2], 80)
#     setServoPulse(10, servo_rate[1]*servo_angle[1]*6.25+1500 + deviation[3], 80)
#     setServoPulse(6, servo_rate[0]*servo_angle[2]*6.25+1500 + deviation[0], 80)
#     setServoPulse(8, servo_rate[1]*servo_angle[3]*6.25+1500 + deviation[1], 80)
#     sleep(sleepTime)

# def move(linear, angular):
#     linear_x, _, _ = linear.x, linear.y, linear.z
#     _, _, angular_z = angular.x, angular.y, angular.z
        
#     forward(servo_angle = [20, 0, 0, -20], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

#     forward(servo_angle = [-38, 0, 0, 38], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

#     forward(servo_angle = [-40, -40, 40, 40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

#     forward(servo_angle = [0, -20, 20, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

#     forward(servo_angle = [0, 38, -38, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

#     forward(servo_angle = [40, 40, -40, -40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

# new version ~~~~~~~~~~~
def forward(x ,servo_angle = [40, 40, -40, -40], sleepTime = 1.0, servo_rate = [1.0, 1.0]):
    dedeviation = [-100 ,0, 40, 120]
    setPWMServoPulse(1, int(servo_rate[0]*servo_angle[2]*6.25+1500 + dedeviation[0]), 80)
    sleep(0.0085)
    setPWMServoPulse(2, int(servo_rate[0]*servo_angle[0]*6.25+1500 + dedeviation[2]), 80)
    #                       -0.5 * -38 * 6.5 + 1500 + 40 =              
    sleep(0.0085)
    setPWMServoPulse(3, int(servo_rate[1]*servo_angle[3]*6.25+1500 + dedeviation[1]), 80)
    sleep(sleepTime)
    setPWMServoPulse(4, int(servo_rate[1]*servo_angle[1]*6.25+1500 + dedeviation[3]), 80)
    sleep(0.0085)

    print("motion:", x)
    print("1: ",servo_rate[0]*servo_angle[2]*6.25+1500 + dedeviation[0])
    print("2: ",servo_rate[0]*servo_angle[0]*6.25+1500 + dedeviation[2])
    print("3: ",servo_rate[1]*servo_angle[3]*6.25+1500 + dedeviation[1])
    print("4: ",servo_rate[1]*servo_angle[1]*6.25+1500 + dedeviation[3], "\n")
    



def move_joystick(linear_x, angular_z):
    # linear_x, _, _ = linear.x, linear.y, linear.z
    # _, _, angular_z = angular.x, angular.y, angular.z
        
    forward(1, servo_angle = [20, 0, 0, -20], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    forward(2, servo_angle = [-38, 0, 0, 38], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    forward(3, servo_angle = [-40, -40, 40, 40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    forward(4, servo_angle = [0, -20, 20, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    forward(5, servo_angle = [0, 38, -38, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    forward(6, servo_angle = [40, 40, -40, -40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])
    
if __name__ == '__main__':
    while(True):
        move_joystick(0.5, 1)



#----------------------------------------------------------------------------------------

        


#-----------------------------------------------------------------------------------------

        # test code
        # Board.setPWMServoPulse(1, 1200, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(2, 1200, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(3, 1800, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(4, 1800, 100)
        # sleep(0.5)
        
        # Board.setPWMServoPulse(1, 1800, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(2, 1800, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(3, 1200, 100)
        # sleep(0.001)
        # Board.setPWMServoPulse(4, 1200, 100)
        # sleep(0.5)
        
