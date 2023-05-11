from spike import PrimeHub, MotionSensor, DistanceSensor, MotorPair

hub = PrimeHub()

distance = DistanceSensor('F')
motor_pair = MotorPair('C', 'D')

motor_pair.start_tank(50,50)
distance.wait_for_distance_closer_than(5, 'cm')
motor_pair.stop()

hub.motion_sensor.reset_yaw_angle()

motor_pair.move_tank(180, 'degrees', 50, -50)
motor_pair.start_tank(30, 60)

while True:
    if(hub.motion_sensor.get_yaw_angle() == -90):
        break

motor_pair.move_tank(180, 'degrees', 50, -50)
motor_pair.move_tank(20, 'cm', 50, 50)
