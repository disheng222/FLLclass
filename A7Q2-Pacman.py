from spike import PrimeHub, LightMatrix, Button
from spike.control import Timer
from math import *
import random


def light_up_pixel(hub, index):
    i = floor(index/5)
    j = index % 5
    print("light_up: ",i,",",j)
    hub.light_matrix.set_pixel(i, j, brightness=100)

def light_down_pixel(hub, index):
    i = floor(index/5)
    j = index % 5
    print("light_down: ",i,",",j)    
    hub.light_matrix.set_pixel(i, j, brightness=0)


hub = PrimeHub()

#i indicates the pac-man's current location: 0, 1, ..., 24
i=0
#r represents the bean's random location
r=12

light_up_pixel(hub,r)
while True:
    if(hub.left_button.is_pressed()):
        light_down_pixel(hub,i) #light down the pacman's old location
        i -= 1
        if(i==-1):
            i = 24
        hub.speaker.start_beep()
        hub.left_button.wait_until_released()
        hub.speaker.stop()
    if(hub.right_button.is_pressed()):
        light_down_pixel(hub,i) #light down the pacman's old location
        i += 1
        if(i==25):
            i = 0
        hub.speaker.start_beep()
        hub.right_button.wait_until_released()
        hub.speaker.stop()
    if(i==r):
        hub.speaker.beep(70,0.5)
        hub.left_button.wait_until_released()
        hub.speaker.stop()
        r = random.randint(0,24)
        light_up_pixel(hub,r) #light up the bean's new location
    light_up_pixel(hub, i) #light up the pacman's new location

