from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import random

hub = PrimeHub()
app = App()

class AdvancedSpeaker(object):
    def playCatSound(self):
        L = ['Cat Angry', 'Cat Happy', 'Cat Hiss', 'Cat Meow 1', 'Cat Meow 2', 'Cat Meow 3', 'Cat Purring', 'Cat Whining']
        app.play_sound(L[random.randint(0,7)])
    def playDogSound(self):
        L = ['Dog Bark 1', 'Dog Bark 2', 'Dog Bark 3', 'Dog Whining 1', 'Dog Whining 2']
        app.play_sound(L[random.randint(0,4)])
    def playDoorBellSound(self):
        L = ['Doorbell 1', 'Doorbell 2', 'Doorbell 3']
        app.play_sound(L[random.randint(0,2)])
    def playBeepSound(self):
        hub.speaker.beep(floor(random()*77+44))


advancedSpeaker = AdvancedSpeaker()

hub.light_matrix.show_image('HAPPY')

advancedSpeaker.playDoorBellSound()
