from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Create your objects here.
hub = MSHub()
movement_motors = MotorPair('A', 'B')
right_motor = Motor('A')
color_sensor = ColorSensor('E')


# Write your program here.
hub.speaker.beep()
"""
Wheel rotations need a new variable for one motor.
This is because when one motor turns, it turns in the negative direction and the other moves in the
positive direction.
Can then take motor rotation to calculate wheel spins needed to follow a line.
Not sure if this works since it seems we need to know how many wheel rotations the path will take.
"""


def wheel_degrees_spun(degrees):
    right_motor.set_degrees_counted(0)
    # resets motor count
    movement_motors.set_default_speed(20)
    while right_motor.get_degrees_counted() < degrees:
        # check degrees rolled in wheel counter if less than the degrees passed through the function
        movement_motors.start((color_sensor.get_reflected_light()-50*2)) 
        # similar to Emma's code; gets reflected light value and tries to stick to -50
        # if higher or lower than -50; will steer off until it can detect -50 again
    movement_motors.stop()


line_follow_degrees(720)