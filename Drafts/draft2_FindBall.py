def ScanForBall():
    while True:
        distance = d_sensor.get_distance_cm()
        if distance is not None and distance <= 4:
            LiftArm()
            continue #change to break and add a finish function?
        color = c_sensor.get_color()
        if color == 'black':
            motor_pair.stop()
            while hub.motion_sensor.get_yaw_angle() > -90:
                motor_pair.start_tank(-10, 10)
            motor_pair.stop()
            motor_pair.move(10, 'cm')
            while hub.motion_sensor.get_yaw_angle() < 0:
                motor_pair.start_tank(-10, 10)
            motor_pair.stop()
        else:
            motor_pair.start()

def LiftArm():
    motor_pair.stop()
    wait_for_seconds(2)
    motor_c.run_for_degrees(-45, 10)
    GoHome()

def GoHome():
    while True:
        while hub.motion_sensor.get_yaw_angle() != 90:
            motor_pair.start_tank(-10, 10)
        motor_pair.stop()
        color = c_sensor.get_color()
        if color == 'black':
            motor_pair.stop()
            while hub.motion_sensor.get_yaw_angle() != 180:
                motor_pair.start_tank(-10, 10)
            motor_pair.stop()
            hub.speaker.play_sound('Warp Speed')
        else:
            motor_pair.start()

