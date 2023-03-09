from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


hub = MSHub()


# initialize all motors/sensors
motor_pair = MotorPair('A', 'B')
c_sensor = ColorSensor('E')
timer = Timer()


# set robot speed
motor_pair.set_default_speed(200)

while True:
    color = c_sensor.get_color()
    if color != 'green':
        motor_pair.start(75, 200)
    else:
        motor_pair.start(-75, 200)

