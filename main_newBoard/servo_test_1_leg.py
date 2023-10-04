# from ServoControl import PWMServo
from time import sleep
from gpiozero import AngularServo
servo_motor_id = [19, 18, 10, 6]
servo = []
left_rate = 0.5
right_rate = 1.3
for i in range(4):
     servo.append(AngularServo(servo_motor_id[i]))
     while True:
          # print(servo_rate)
          for i in range(-40, 0, 1):
               servo[0].angle = i
               servo[2].angle = -i
               sleep(0.0025)
          for i in range(-40, 40, 1):
               servo[1].angle = -i
               servo[3].angle = i
               sleep(0.00125)
          for i in range(0, 40, 1):
               servo[0].angle = i
               servo[2].angle = -i
               sleep(0.0025)

          for i in range(40, 0, -1):
               servo[1].angle = -i
               servo[3].angle = i
               sleep(0.0025)
          for i in range(40, -40, -1):
               servo[0].angle = i
               servo[2].angle = -i
               sleep(0.00125)
          for i in range(0, -40, -1):
               servo[1].angle = -i
               servo[3].angle = i
               sleep(0.0025)
# servo = PWMServo()
# servo.setPulse(2, 2000)
# servo.setPulse(4, 2000)
# servo.setPulse(6, 1000)
# servo.setPulse(8, 1000)
# sleep(1)
# # servo.updatePulse(-1)
# while True:
#      servo.generate_walking_gait(2)
#      servo.generate_walking_gait(4)
#      servo.generate_walking_gait(6)
#      servo.generate_walking_gait(8)
#      sleep(0.05)


# def generate_walking_gait(id):
#     max_pulse = 1800
#     low_speed_pulse = 1750
#     min_pulse = 1200
#     resolution = 80
    
#     leg_next_step = {2:0, 4:0, 6:0, 8:0}
#     updatePulse(-1)
#     if id == 2:
#         if status[id] == 0:
#             leg_next_step[id] = getServoPulse(id)+resolution - getServoDeviation(id)
#             if leg_next_step[id] >= max_pulse:
#                 status[id] = 1
#         elif status[id] == 1 and getServoPulse(id) >= low_speed_pulse:
#             leg_next_step[id] = getServoPulse(id)-resolution/2

#         else:
#             leg_next_step[id] = getServoPulse(id)-resolution*3/2 - getServoDeviation(id)

#             if leg_next_step[id] <= min_pulse:
#                 status[id] = 0
#         setServoPulse(id, leg_next_step[id],0)

#     if id == 6:
#         if status[id] == 0:
#             leg_next_step[id] = getServoPulse(id)+resolution
#             if leg_next_step[id] >= max_pulse:
#                 status[id] = 1
#         elif status[id] == 1 and getServoPulse(id) >= low_speed_pulse:
#             leg_next_step[id] = getServoPulse(id)-resolution/2

#         else:
#             leg_next_step[id] = getServoPulse(id)-resolution*3/2

#             if leg_next_step[id] <= min_pulse:
#                 status[id] = 0
#         setServoPulse(id, leg_next_step[id],0)

#     if id == 4:
#         if status[id] == 0 and getServoPulse(id) <= 1250:
#             leg_next_step[id] = getServoPulse(id)+resolution/2 - getServoDeviation(id)

#         elif status[id] == 0 :
#             leg_next_step[id] = getServoPulse(id)+resolution*3/2 - getServoDeviation(id)
#             if leg_next_step[id] >= max_pulse:
#                 status[id] = 1
#         else:
#             leg_next_step[id] = getServoPulse(id)-resolution - getServoDeviation(id)

#             if leg_next_step[id] <= min_pulse:
#                 status[id] = 0
#         print(getServoPulse(id))
#         setServoPulse(id, leg_next_step[id],0)
#         # print(status4 , servo_pwm_now[4])
        
#     if id == 8:
#         if status[id] == 0 and getServoPulse(id) <= 1250:
#             leg_next_step[id] = getServoPulse(id)+resolution/2

#         elif status[id] == 0 :
#             leg_next_step[id] = getServoPulse(id)+resolution*3/2
#             if leg_next_step[id] >= max_pulse:
#                 status[id] = 1
#         else:
#             leg_next_step[id] = getServoPulse(id)-resolution

#             if leg_next_step[id] <= min_pulse:
#                 status[id] = 0
#         setServoPulse(id, leg_next_step[id],0)