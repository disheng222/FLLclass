from spike import PrimeHub, MotionSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motors = MotorPair('C','D')

hub.motion_sensor.reset_yaw_angle()


motors.set_default_speed(30)
motors.start(0)
while True:
    motors.start(-5*hub.motion_sensor.get_yaw_angle())
    print(hub.motion_sensor.get_yaw_angle())
