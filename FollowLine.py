from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

def follow_line():
    """
    Follow green track and avoid black border.

    A function that makes the robot follow the green track and avoid black border.

    :precondition: line is green and border is black.
    :postcondition: robot follows the green track and avoids black line.
    """
    hub = MSHub()


    # initialize all motors/sensors
    motor_pair = MotorPair('B', 'A')
    motor_a = Motor('A')
    motor_b = Motor('B')
    motor_c = Motor('C')
    d_sensor = DistanceSensor('D')
    c_sensor = ColorSensor('E')


    # set robot speed
    motor_pair.set_default_speed(-200)


    # assume that the robot starts on the track
    motor_pair.start()


    # do zig-zags with the robot until we reach end of the track
    while True:
        color = c_sensor.get_color()
    #color = c_sensor.wait_for_new_color()


    # by convention, steer to the left
        if color == 'green':
            motor_pair.start(75, -200)
        else:
            motor_pair.start(-75, -200)