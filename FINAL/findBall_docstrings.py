from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor
from mindstorms.control import wait_for_seconds, Timer

# Create your objects here.

hub = MSHub()
motor_pair = MotorPair('A', 'B')
motor_c = Motor('C')
c_sensor = ColorSensor('E')
d_sensor = DistanceSensor('F')
timer = Timer()


def main():
    """
    Runs the program.

    Makes the hub beep, sets default speed to 20%, and calls scan function.
    """
    hub.speaker.beep()
    motor_pair.set_default_speed(20)
    scan()


def scan():
    """
    Detects an object, lifts its arm and then returns to the starting position.

    A function that makes the robot move forward but if it detects black or white,
    makes it reverse.  If it sees an object, picks it up and goes back to center.
    """
    hub.motion_sensor.reset_yaw_angle()
    timer.reset()
    while True:
        distance = d_sensor.get_distance_cm()
        if c_sensor.get_color() == 'white' or c_sensor.get_color() == 'black':
            motor_pair.stop()
            motor_pair.move(timer.now(), 'seconds', 0, -20)
            rotate()
            timer.reset()
        else:
            motor_pair.start()
        if distance is not None and distance <= 8:
            final_time = timer.now()
            lift_arm()
            motor_pair.move(final_time, 'seconds', 0, -20)
            break
    finish()


def rotate():
    """
    Makes robot spin in 20 degree increments.
    """
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() < 20:
        motor_pair.start_tank(10, -10)
    motor_pair.stop()


def lift_arm():
    """
    Stops for 2 seconds and lifts arm.
    """
    motor_pair.stop()
    wait_for_seconds(2)
    motor_c.run_for_degrees(75, 20)


def finish():
    """
    Stops robot and plays a sound.
    """
    motor_pair.stop()
    hub.speaker.play_sound("Ha Ha Ha")


main()