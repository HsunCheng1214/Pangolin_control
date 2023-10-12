import Board
import time

print('''
**********************************************************
********功能:幻尔科技树莓派扩展板，直流电机控制例程**********
**********************************************************
----------------------------------------------------------
Official website:http://www.lobot-robot.com/pc/index/index
Online mall:https://lobot-zone.taobao.com/
----------------------------------------------------------

----------------------------------------------------------
Usage:
    sudo python3 MotorControl.py
----------------------------------------------------------
Version: --V1.0  2021/08/16
----------------------------------------------------------
Tips:
 * 按下Ctrl+C可关闭此次程序运行，若失败请多次尝试！
----------------------------------------------------------
''')

# Board.setMotor(电机编号, 电机速度)
# 电机编号（1～4），电机速度（-100～100），正值为正转，负值为反转
def motor(): # 启动电机
	Board.setMotor(2, 100) #马达1,以100速度正转 
	time.sleep(3)
	Board.setMotor(2, 0)
	time.sleep(1)
	Board.setMotor(2, -50) #马达1,以-50速度反转
	time.sleep(3)
	Board.setMotor(2, 0)

def stop(): # 关闭电机
	Board.setMotor(2, 0)	

if __name__ == '__main__':
	try:
		motor()
	except KeyboardInterrupt:
		stop()
 

