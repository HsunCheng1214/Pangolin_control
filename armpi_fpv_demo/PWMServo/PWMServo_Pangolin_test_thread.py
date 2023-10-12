import time
import threading
import Board
import sys
sys.path.append('/home/ubuntu/ArmPi/HiwonderSDK/PWMServo')

print("Pangolin feet test ~~~~~~~")

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
def feet1():
    while(True):
        Board.setPWMServoPulse(1, 1200, 100)
        time.sleep(0.5)
        Board.setPWMServoPulse(1, 1800, 100)
        time.sleep(0.5)
        print("feet 1 move")

def feet2():
    while(True):
        Board.setPWMServoPulse(2, 1200, 100)
        time.sleep(0.5)
        Board.setPWMServoPulse(2, 1800, 100)
        time.sleep(0.5)
        print("feet 2 move")

def feet3():
    while(True):
        Board.setPWMServoPulse(3, 1800, 100)
        time.sleep(0.5)
        Board.setPWMServoPulse(3, 1200, 100)
        time.sleep(0.5)
        print("feet 3 move")

def feet4():
    while(True):
        Board.setPWMServoPulse(4, 1800, 100)
        time.sleep(0.5)
        Board.setPWMServoPulse(4, 1200, 100)
        time.sleep(0.5)
        print("feet 4 move")

f1 = threading.Thread(target = feet1)
f2 = threading.Thread(target = feet2)
f3 = threading.Thread(target = feet3)
f4 = threading.Thread(target = feet4)

if __name__ == '__main__':
    f1.start()
    f2.start()
    f3.start()
    f4.start()

