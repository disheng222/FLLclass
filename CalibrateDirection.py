'''
This code is used to calibrate the direction based on black lines
'''
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
colorE = ColorSensor('F')
colorF = ColorSensor('E')

motorA = Motor('A')
motorB = Motor('B')

motorA.start(speed=10)
motorB.start(speed=-10)

foundA = False
foundB = False

i = 0
while (not foundA or not foundB):
    print(i)
    if (colorE.get_color()=="black"):
        motorB.stop()
        print('foundB')
        foundB = True
    if (colorF.get_color()=="black"):
        motorA.stop()
        print('foundA')
        foundA = True
    i=i+1
print('out....')

foundA = False
foundB = False
motorA.start(speed=10)
motorB.start(speed=-10)
wait_for_seconds(1)
i = 0
while (not foundA or not foundB):
    print(i)
    if (colorE.get_color()=="black"):
        motorB.stop()
        print('foundB')
        foundB = True
    if (colorF.get_color()=="black"):
        motorA.stop()
        print('foundA')
        foundA = True
    i=i+1
