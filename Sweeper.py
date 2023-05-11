from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

distance_sensor = DistanceSensor('F')
motors = MotorPair('C','D')

while True:
    motors.start(0, 50)
    distance_sensor.wait_for_distance_closer_than(20, 'cm')
    #motors.stop()
    motors.move_tank(180, 'degrees', 50, -50)
