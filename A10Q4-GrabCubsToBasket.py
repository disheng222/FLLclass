#Note that the robot's right side should be 6.5 inch to the square basket at the beginning
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def moveForSeconds(motion_sensor, motor_pair, timer, speed, secs):
    motor_pair.set_default_speed(speed)
    timer.reset()
    while True:
        motor_pair.start(5*motion_sensor.get_yaw_angle())
        current = timer.now()
        if(current >= secs):
            motor_pair.stop()
            break

def turnRightandPutDownObject(motion_sensor, motor_pair, claw):
    motor_pair.start_tank(5,-5) #make a right turn
    while True:
        if(motion_sensor.get_yaw_angle() >= 86):
            motor_pair.stop()
            motor_pair.move(-1.5,'in') #move forward by 0.5 inch
            claw.run_for_rotations(1,20)
            break

def turnLeftandPutDownClaws(motion_sensor, motor_pair, claw):
    motor_pair.start_tank(-5,5)
    while True:
        if(motion_sensor.get_yaw_angle() <= 0):
            motor_pair.stop()
            claw.run_for_rotations(1.1,20)
            break

hub = PrimeHub()
color_sensor1 = ColorSensor('E')
color_sensor2 = ColorSensor('F')
motor_pair = MotorPair('A','B')
claw = Motor('C')
distance_sensor = DistanceSensor('D')
motion_sensor = MotionSensor()

motor_pair.set_default_speed(20)
motion_sensor.reset_yaw_angle()

timer = Timer()

timer.reset()

while True:
    motor_pair.start(-5*hub.motion_sensor.get_yaw_angle())
    #print(hub.motion_sensor.get_yaw_angle(), distance_sensor.get_distance_cm())

    distance = distance_sensor.get_distance_cm()
    if(str(distance)=="None"):
        continue
    if(distance <= 5):
        targetTime = timer.now()+0.5 #record how much time it took to walt to the object
        #print("targetTime=",targetTime)
        motor_pair.stop()
        claw.run_for_rotations(-0.93,20) #grab the object
        moveForSeconds(motion_sensor, motor_pair, timer, -20, targetTime) #move backward

        turnRightandPutDownObject(motion_sensor, motor_pair, claw) #turn right and put down object

        motor_pair.move(1.5,'in') #move backward
        claw.run_for_rotations(-1.1,20) #Restore the claw back to the initial position

        turnLeftandPutDownClaws(motion_sensor, motor_pair, claw) #turn left and put down claws

        motor_pair.set_default_speed(20) #reset the default speed so that the robot will move forward again
        timer.reset()        #reset the timer for checking how far the next object is


