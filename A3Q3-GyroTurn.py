from spike import PrimeHub, ForceSensor, MotionSensor, DistanceSensor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.motion_sensor.reset_yaw_angle()
motor_pair = MotorPair('C','D')

#move 2 cm
motor_pair.move_tank(10, 'cm', 50, 50)
motor_pair.start_tank(-30,30)
while True:
    if(hub.motion_sensor.get_yaw_angle() < -30):
        break
motor_pair.stop()

motor_pair.move_tank(10, 'cm', 50, 50)
motor_pair.start_tank(30,-30)
while True:
    if(hub.motion_sensor.get_yaw_angle() > 30):
        break
motor_pair.stop()

motor_pair.move_tank(20, 'cm', 50, 50)
motor_pair.start_tank(-30,30)
while True:
    if(hub.motion_sensor.get_yaw_angle() < -30):
        break
motor_pair.stop()

motor_pair.move_tank(10, 'cm', 50, 50)
motor_pair.start_tank(30,-30)
while True:
    if(hub.motion_sensor.get_yaw_angle() == 0):
        break
motor_pair.stop()

motor_pair.move_tank(10, 'cm', 50, 50)
