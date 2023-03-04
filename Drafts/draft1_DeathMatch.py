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

motor_pair.set_default_speed(25)

"""
How this works:
Assuming the border is a box or a circle, the robot will stay in one spot and continuously spins in place
until it can find an object near it and rams into it.If the color sensor detects the border (assuming
black tape is used), then it reverses.
Continues to do this forever.
"""

def spin():
    motor_pair.start_tank(-10, 10)

def ram(movement):
    motor_pair.start_tank(+movement, -movement)

while True:
    distance = distance_sensor.get_distance_cm()
    if color_sensor.get_color() == 'black':
            motor_pair.start(-75)
            wait_for_seconds(0.5)
    elif distance == None:
        motor_pair.start(50)
    elif distance <= 50:
        motor_pair.start(50)
    else:
        spin

