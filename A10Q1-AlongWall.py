from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def right_turn87(motor_pair, hub):
    motor_pair.start_tank(15,-15)
    while True:
        if(hub.motion_sensor.get_yaw_angle() > 87):
            break 
    motor_pair.stop()

def right_turn86(motor_pair, hub):
    motor_pair.start_tank(15,-15)
    while True:
        if(hub.motion_sensor.get_yaw_angle() > 87):
            break
    motor_pair.stop()

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

hub = PrimeHub()
hub.motion_sensor.reset_yaw_angle()
motor_pair = MotorPair('A','B')

distanceSensor = DistanceSensor('C')
motor_pair.set_default_speed(90)
motor_pair.start(0)

i = 0
while True:
    motor_pair.start(-3*hub.motion_sensor.get_yaw_angle())
    distance = distanceSensor.get_distance_cm()
    if(str(distance)=="None"):
        continue
    if(distance<7):
        if(i%2==0):
            right_turn87(motor_pair, hub)
        else:
            right_turn86(motor_pair, hub)
        hub.motion_sensor.reset_yaw_angle()
        motor_pair.start(0)
        i=i+1


