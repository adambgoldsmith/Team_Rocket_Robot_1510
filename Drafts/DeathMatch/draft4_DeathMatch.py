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
def sumo():
    while True:
        distance = distance_sensor.get_distance_cm()
        if color_sensor.get_color() == 'black':
            motor_pair.start(0, -50)
            wait_for_seconds(0.5)
        elif distance == None:
            distance_sensor.light_up_all(50)
            motor_pair.start(0, 50)
        elif distance <= 15:
            distance_sensor.light_up_all(50)
            motor_pair.start(0, 50)
        else:
            motor_pair.start(20, 0)
sumo()
def main():
    print(sumo)