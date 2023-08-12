from spike import PrimeHub, MotionSensor, MotorPair, ColorSensor
from spike.control import wait_for_seconds, Timer
from math import *

class AdvancedMotorPair(MotorPair):
    def __init__(self, port1, port2):
        super().__init__(port1, port2)

    def turnRight(self, speed=20, degree=90):
        super().move_tank(2*degree, 'degrees', speed, -speed)

    def turnLeft(self, speed=20, degree=90):        
        super().move_tank(2*degree, 'degrees', -speed, speed)

    def moveStraight(self, speed=20, seconds=2):
        hub = PrimeHub()
        hub.motion_sensor.reset_yaw_angle()
        timer = Timer()
        super().set_default_speed(speed)
        super().start(0)
        while True:
            print(timer.now(), ", ", seconds)
            if(timer.now() >= seconds):
                #print("===============")
                super().stop()
                break
            super().start(-5*hub.motion_sensor.get_yaw_angle())
            #print("moveStraight:",hub.motion_sensor.get_yaw_angle()," ",timer.now())

    def binaryLineFollower(self, port='A', color='black', speed=20, seconds=2):
        timer = Timer()
        colorSensor = ColorSensor(port)
        while(True):
            if(timer.now() > seconds):
                super().stop()
                break;
            if(colorSensor.get_color()==color):
                super().start_tank(20,10)
            else:
                super().start_tank(10,20)
            #print("binaryLineFollower")    

    def proportionalLineFollower(self, port='A', speed=20, seconds=2):
        timer = Timer()
        colorSensor = ColorSensor(port)
        super().set_default_speed(10)
        steering = 0
        while(True):
            if(timer.now() >= seconds):
                super().stop()
                break;
            steering = 2*(colorSensor.get_reflected_light()-55)
            super().start(steering)
        #print("proportionalLineFollower")    

hub = PrimeHub()
motorPair = AdvancedMotorPair('B','C')
motorPair.move(5,'cm')
motorPair.turnRight(20, 90)
motorPair.move(5,'cm')
motorPair.turnLeft(20, 90)
motorPair.move(5,'cm')
motorPair.turnRight(20,145)
motorPair.moveStraight(20,2)
motorPair.binaryLineFollower('A', 'black', 20, 2)
motorPair.proportionalLineFollower('A', 20, 2)
