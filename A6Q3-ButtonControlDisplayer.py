from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
class ButtonControlDisplayer(object): #object is basic class, buttoncontroldisplayer is the derived class of object, dont ask questions
    def __init__(self, hub): #now we got to define hub as it is a pareameter of the constructer function: we gotta define hub for future use in this class
        self.hub = hub #now we use self.hub as it is a variable in this class
        self.n_init = True #this information is for number: check if the number form was called for the first time
        self.c_init = True #this is for character
        self.cv = -2  #this is the current value of the number form: not this number
        self.vc=-3 #this is the current value of the letter form: not this exact number

    def buttonControlNumbers(self, min, max): #this is called buttoncontrolnumbers as we are supposed to call it that. min max used as values we will use.  
        if self.n_init==True: #as we can see from the past, it checks if this is the first time that this is being called. AKA being used. not first, go past
            self.cv=floor((min+max)/2) #because this is the first time, it puts the mean of the numbers and makes the variable, cv into th mean of the numbers.
            self.n_init=False #now it go false as function called

        hub.light_matrix.write(self.cv) #writes the mean

        if hub.left_button.was_pressed(): 
            self.cv=(self.cv-1)
            if self.cv<=min:
                self.cv=min
            hub.light_matrix.write(self.cv)

        if hub.right_button.was_pressed():
            self.cv=(self.cv+1)
            if self.cv>=max:
                self.cv=max
            hub.light_matrix.write(self.cv)

    def buttonControlLetter(self, min, max):
        if self.c_init==True:
            self.vc=floor((ord(min)+ord(max))/2)
            self.c_init=False
        
        hub.light_matrix.write(chr(self.vc))

        if hub.left_button.was_pressed():
            self.vc=self.vc-1
            if self.vc<=ord(min):
                self.vc=ord(min)
            hub.light_matrix.write(chr(self.vc))

        if hub.right_button.was_pressed():
            self.vc=self.vc+1
            if self.vc>=ord(max):
                self.vc=ord(max)
            hub.light_matrix.write(chr(self.vc))

colorsensor= ColorSensor('B')
buttoncontrol= ButtonControlDisplayer(hub)
while True:
    x=colorsensor.get_color()
    if x=='black':
        buttoncontrol.buttonControlLetter('a', 'z')
    if x=='white':
        buttoncontrol.buttonControlNumbers(1, 9)
    if x==None:
        hub.light_matrix.show_image('SAD')
