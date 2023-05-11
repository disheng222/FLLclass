from spike import ForceSensor, MotionSensor, DistanceSensor, MotorPair
from spike.control import Timer
from math import *
from spike.operator import equal_to

motors = MotorPair('C','D')
forceSensor = ForceSensor('A')
distanceSensor = DistanceSensor('F')
timer = Timer()
target_distance = 0
current_distance = 0
tartet_time = 0

#set the default constant speed
motors.set_default_speed(20)

#go into the while loop to bypass object
while True:
    motors.start(0) #start with steering angle of 0
    forceSensor.wait_until_pressed()
    motors.move_tank(180, 'degrees', 20, -20) #when hit the wall, turn right immediately.
    motors.start(0) #keep moving stright forward
    target_distance = distanceSensor.get_distance_cm() #use the distance sensor to control the same distance to the wall
    timer.reset() #use the timer to record how far the robot would move along the wall
    while True:
        current_distance = distanceSensor.get_distance_cm()
        if(str(current_distance)=="None" or current_distance>50): #if current distance is greater than a threshold
            target_time = timer.now() #then, it means the robot moved out of range
            motors.move(15, 'cm', 0) #then, keep moving 10 cm to ensure it completely passed the wall edge
            break
        #distance control to make sure the robot is moving along the wall
        print(current_distance," ",target_distance)
        motors.start(5*(target_distance-current_distance))

    motors.move_tank(180, 'degrees', -20, 20) #turn left
    motors.move(15, 'cm', 0) #move 10 cm to make sure the robot's distance sensor can detect the wall
    motors.start(0)
    target_distance = distanceSensor.get_distance_cm()
    while True:
        current_distance = distanceSensor.get_distance_cm()
        print("-->",str(current_distance))
        if(str(current_distance)=="None" or current_distance>50):
            motors.move(15, 'cm', 0)
            break
        motors.start(5*(target_distance-current_distance))         

    motors.move_tank(180, 'degrees', -20, 20)
    motors.move(15, 'cm', 0)
    motors.start(0)
    target_distance = distanceSensor.get_distance_cm()
    timer.reset()    
    while True:
        current_distance = distanceSensor.get_distance_cm()

        if(timer.now()>target_time):
            motors.move_tank(180, 'degrees', 20, -20)
            break
        motors.start(5*(target_distance-current_distance))
