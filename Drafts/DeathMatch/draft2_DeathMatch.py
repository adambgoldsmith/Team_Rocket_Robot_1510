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
How this works:
Assuming the border is a box or a circle, the robot will stay in one spot and continuously spins in place
until it can find an object near it and rams into it.If the color sensor detects the border (assuming
black tape is used), then it reverses.
Continues to do this forever.
"""


def sumo():
    # hub_degrees.reset_yaw_angle()
    while True:
        distance = distance_sensor.get_distance_cm()
        if color_sensor.get_color() == 'black':
            # hub_degrees.get_yaw_angle()
            # while hub_degrees.get_yaw_angle() != (abs(45)):
            # motor_pair.start_tank(50, -50)
            # motor_pair.move_tank(3, 'cm', -50, 50)
            motor_pair.start(-50)
            wait_for_seconds(2)
        elif distance == None:
            distance_sensor.light_up_all(50)
            motor_pair.start(30)
        elif distance <= 10:
            distance_sensor.light_up_all(50)
            motor_pair.move(100)
        else:
            motor_pair.start_tank(20, -20)

sumo()

def main():
    print(sumo)