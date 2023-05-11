from spike import PrimeHub, ColorSensor, MotorPair
from math import *
import time

hub = PrimeHub()
color = ColorSensor('A')
motor_pair = MotorPair('B', 'C')
integral = 0
lastError = 0
while True:
    error = color.get_reflected_light() - 55
    P_fix = error * 0.7
    integral = integral + error # or integral+=error
    I_fix = integral * 0.002
    derivative = error - lastError
    lastError = error
    D_fix = derivative * 3.5
    correction = P_fix + I_fix + D_fix
    #correction = P_fix + I_fix
    #print(P_fix,"+",I_fix,"+",D_fix,"=",correction)
    time.sleep(0.03)
    #motor_pair.start_tank_at_power(int(20+correction), int(20-correction))
    motor_pair.start_tank(int(15-correction),int(15+correction))
