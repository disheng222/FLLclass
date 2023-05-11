def judge_cargo(motor_pair, distance_sensor):
    dis1 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(50, 'degrees', 30, -30)
    dis2 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(100, 'degrees', -30, 30)
    dis3 = distance_sensor.get_distance_cm()
    motor_pair.move_tank(50, 'degrees', 30, -30)
    if(str(dis1)=="None" or str(dis2)=="None" or str(dis3)=="None"):
        return True
    if(dis1 < 10 and dis2 < 10 and dis3 < 10):
        return False #Front is the wall
    else:
        return True #Front is an object
