from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
# Write your program here.
hub.speaker.beep()
motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('E')
distance_sensor = DistanceSensor('D')
hub_degrees = hub.motion_sensor
motor_pair.set_default_speed(25)

"""
Robot scans arena to see if there are any objects in the arena.

If there are, then the robot runs towards it.  
There isn't, then it spins around. 
When it detects the border, it reverses. 
"""


def sumo():
    while True:
    # forever loop
        distance = distance_sensor.get_distance_cm()
        # initializes distance
        if color_sensor.get_color() == 'black':
            motor_pair.start(0, -50)
            wait_for_seconds(0.5)
            motor_pair.stop()
            # if robot detects border, then reverse for 0.5 seconds and stops
        elif distance == None:
            distance_sensor.light_up_all(50)
            motor_pair.start(0, 50)
            # if distance is none, then ram into robot
            # this is necessary or else Mindstorms will give an error
        elif distance <= 15:
            distance_sensor.light_up_all(50)
            motor_pair.start(0, 50)
            # if distance is 15cm or under, then robot rams into other robot
        else:
            motor_pair.start_tank(30, -30)
            # if there are no objects in the distance, spin around

sumo()


def main():
    print(sumo)