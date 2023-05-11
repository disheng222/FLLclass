from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

def straight_line_move_and_turn(motors, timer, target_yaw_angle):
    hub.motion_sensor.reset_yaw_angle()
    motors.start(0)
    timer.reset()   
    while True:
        motors.start(8*(target_yaw_angle - hub.motion_sensor.get_yaw_angle()))
        if(timer.now() >= 4):
            degrees = 2*(90 - hub.motion_sensor.get_yaw_angle())
            motors.move_tank(degrees, 'degrees', 30, -30)
            break


motor_pair = MotorPair('C', 'D')
motor_pair.set_default_speed(20)
hub.motion_sensor.reset_yaw_angle()
timer = Timer()
motor_pair.start(0)

for i in range(12):
    straight_line_move_and_turn(motor_pair, timer, 0)




