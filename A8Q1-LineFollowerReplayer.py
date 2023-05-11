from spike import PrimeHub, Button, ForceSensor, ColorSensor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import time


class LineFollowAgent(object):

    def __init__(self, color_port, motor_port1, motor_port2, force_port):
        self.hub = PrimeHub()
        self.color = ColorSensor('A')
        self.motor_pair = MotorPair('B', 'C')
        self.force_sensor = ForceSensor('D')
        self.error_list = [0]
        self.checkpoint = 0

    def PIDLineFollower(self):
        self.error_list.clear()
        self.checkpoint = 0

        integral = 0
        lastError = 0

        while True:
            if(self.hub.left_button.was_pressed()):
                self.motor_pair.stop()
                break
            error = self.color.get_reflected_light() - 55
            self.error_list.append(error)
            P_fix = error * 0.7
            integral = integral + error # or integral+=error
            I_fix = integral * 0.002
            derivative = error - lastError
            lastError = error
            D_fix = derivative * 3.5
            correction = P_fix + I_fix + D_fix
            #print(P_fix,"+",I_fix,"+",D_fix,"=",correction)
            time.sleep(0.03)
            self.motor_pair.start_tank(int(10-correction),int(10+correction))

    def PIDLineFollowReplay(self):
        integral = 0
        lastError = 0
        i = self.checkpoint
        size = len(self.error_list)
        while True:
            if(i>=size):
                i = 0
                self.motor_pair.stop()
                break
            error = self.error_list[i]
            if(self.hub.left_button.was_pressed()):
                self.motor_pair.stop()
                break        
            P_fix = error * 0.7
            integral = integral + error # or integral+=error
            I_fix = integral * 0.002
            derivative = error - lastError
            lastError = error
            D_fix = derivative * 3.5
            correction = P_fix + I_fix + D_fix
            time.sleep(0.03)
            self.motor_pair.start_tank(int(10-correction),int(10+correction))
            i += 1

        self.checkpoint = i


agent = LineFollowAgent('A','B','C','D')
while True:
    if(agent.hub.right_button.was_pressed()):
        agent.PIDLineFollowReplay()
    if(agent.force_sensor.is_pressed()):
        agent.PIDLineFollower()


