'''
This code is used to calibrate the direction based on black lines
'''

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
left_wheel = Motor('B')
right_wheel = Motor('A')
color_sensor_right = ColorSensor('E')
color_sensor_left = ColorSensor('F')

hub.light_matrix.show_image('HAPPY')

left_wheel.start(-20)
right_wheel.start(20)

while True:
    color1 = color_sensor_right.get_color()
    color2 = color_sensor_left.get_color()

    if color1 == 'black':
        left_wheel.stop()
        if color_sensor_left.get_color() == 'black':
            right_wheel.start(20)

    if color2 == 'black':
        right_wheel.stop()
        if color_sensor_right.get_color() == 'black':
            left_wheel.start(-20)
