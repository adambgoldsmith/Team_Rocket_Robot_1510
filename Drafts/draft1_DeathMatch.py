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


# If it touches
def ram(movement, spin):
    motor_pair.start_tank(-movement-spin, movement+spin)
    # start tank function given by API
    # replaced number values with the two values that go through the function
        # in this case, movement and spin


while True:
    # forever loop
    distance = distance_sensor.get_distance_cm()
    # don't want to get a distance value of none so initialize distance variable to the method .get distance to the distance sensor
    # get distance is a built in API method
    # _cm() gets the distance in cm
    if color_sensor.get_color() == 'black':
        # if color sensor sees black means the back of the robot is over black line (assuming border is black)
            ram(-75, 0)
            # move -75 (in reverse, 100 is top speed so this is relatively fast)
            # moves both motors simultaneously
            wait_for_seconds(0.5)
            # keeps reversing for half a second
    elif distance == None:
        # if distance value records a value of None, want to treat it like a robot is on the other side
        ram(50, 0)
        # 50 is half of top speed but can be adjusted to go faster or slower
    elif distance <= 50:
        # this is similar to above code; if something is less than 50 cm in front of Tricky, then
        # assume that there is a robot there and ram into it
        ram(50, 0)
    else:
        ram(0, 20)
        # if the color sensor does not detect black or an object
        # then do not want the robot to move backwards or forwards and instead turn in place