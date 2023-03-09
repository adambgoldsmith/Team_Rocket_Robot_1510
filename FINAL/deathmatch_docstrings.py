from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, \
    less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
# Write your program here.
hub.speaker.beep()
motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('E')
distance_sensor = DistanceSensor('F')
hub_degrees = hub.motion_sensor
motor_pair.set_default_speed(100)
timer = Timer()

def sumo():
    """
    Spins in place or if it sees an objects, runs into it
    while avoiding the border.

    To avoid the border, the robot detects if it sees black and if it does,
    it reverses.
    :param:
    :precondition: try to stay in green arena and run into objects
    :postcondition: spin around if no objects detected, else run into objects
    while reversing if it sees black
    :return: robot that knocks other robots out of a ring while staying inside it
    """

    motor_pair.start_tank(50, -50)
    while True:
        # forever loop
        distance = distance_sensor.get_distance_cm()
        # initializes distance
        if color_sensor.get_color() != 'green':
            motor_pair.move(25, 'cm', 0, -100)
            # if robot detects border, then reverse for 0.5 seconds and stops
        elif distance is None or distance >= 15:
            motor_pair.start_tank(50, -50)
            # if distance is none, then ram into robot
            # this is necessary or else Mindstorms will give an error
        elif distance <= 6:
            distance_sensor.light_up_all(50)
            motor_pair.start(0, 100)
            # if distance is 15cm or under, then robot rams into other robot
        if timer.now() >= 10:
            while True:
                if color_sensor.get_color() != 'green':
                    motor_pair.move(25, 'cm', 0, -100)
                    timer.reset()
                    break
                else:
                    motor_pair.start()


sumo()
