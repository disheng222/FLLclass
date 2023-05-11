from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def judge_cargo(motor_pair, distance_sensor):
    dis1 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(50, 'degrees', 30, -30)
    dis2 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(100, 'degrees', -30, 30)
    dis3 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(50, 'degrees', 30, -30)    
    if(str(dis1)=="None" or str(dis2)=="None" or str(dis3)=="None"): #this could be ignored on the FLL table because of the walls (impossible to get none value for distance in that case)
        #print("str=",str(dis1))
        return True
    if(dis1 < 10 and dis2 < 10 and dis3 < 10):
        return False    #Front is the wall
    else:
        return True    #Front is an object

def search_object(motor_pair, target_yaw, distance_sensor):
    print("search object")
    motor_pair.set_default_speed(30)
    distance_sensor.wait_for_distance_closer_than(5,'cm')
    return(judge_cargo(motor_pair, distance_sensor))

def backward_move(motor_pair, speed, target_yaw, force_sensor):
    motor_pair.set_default_speed(speed)
    
    while True:
        steering=5*(hub.motion_sensor.get_yaw_angle()-target_yaw)
        print("target_yaw=",target_yaw,"current_yaw=", hub.motion_sensor.get_yaw_angle(),"steering=",steering)
        motor_pair.start(steering)
        if(force_sensor.is_pressed()):
            print("force_sensor pressed")
            motor_pair.stop()
            break

def grab_object(lifter):
    lifter.set_default_speed(20)
    lifter.run_for_degrees(-130)

def move_object(motors, target_yaw, force_sensor):
    if(target_yaw > 0): # face forward
        backward_move(motors, -30, target_yaw, force_sensor)
    else: # face backward
        motors.move_tank(180, 'degrees', 30, -30)
        backward_move(motors, -30, target_yaw, force_sensor)


hub = PrimeHub()

hub.motion_sensor.reset_yaw_angle()

force_sensor = ForceSensor('A')
motor_pair = MotorPair('C','D')
distance_sensor = DistanceSensor('F')
lifter = Motor('E')

motor_pair.move_tank(180, 'degrees', 30, -30) #turn right, now the yaw angle is 90
target_yaw = 90
motor_pair.start(0,30)

while True:
    motor_pair.start(0,30)
    s = search_object(motor_pair, target_yaw, distance_sensor)
    if(s): #an object is in front
        grab_object(lifter)
        move_object(motor_pair, target_yaw, force_sensor)
        lifter.run_for_degrees(130)
        wait_for_seconds(3) #wait for you to collect the object
    else: # wall is in front, two cases: front end wall or back-end wall
        #print("hub.motion_sensor.get_yaw_angle()=",hub.motion_sensor.get_yaw_angle())
        if(hub.motion_sensor.get_yaw_angle()>0):
            motor_pair.move_tank(180, 'degrees', -30, 30) #turn left
            motor_pair.move_tank(11.2, 'cm', 30, 30)
            motor_pair.move_tank(180, 'degrees', -30, 30) #turn left
        else:
            motor_pair.move_tank(180, 'degrees', 30, -30) #turn right
            motor_pair.move_tank(11.2, 'cm', 30, 30)
            motor_pair.move_tank(180, 'degrees', 30, -30) #turn right
        

