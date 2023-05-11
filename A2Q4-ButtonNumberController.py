from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

old_value = 0
new_value = 0

hub.light_matrix.write(new_value)
while True:
    if(hub.left_button.is_pressed()):
        new_value -= 1
        hub.speaker.start_beep()
        hub.left_button.wait_until_released()
        hub.speaker.stop()
    if(hub.right_button.is_pressed()):
        new_value += 1
        hub.speaker.start_beep()
        hub.right_button.wait_until_released()
        hub.speaker.stop()
    if(new_value < 0):
        new_value = 0
    if(new_value > 9):
        new_value = 9
    if(old_value != new_value):
        hub.light_matrix.write(new_value)
        print(new_value)
        old_value = new_value

