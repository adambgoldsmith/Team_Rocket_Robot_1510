from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
motor_c = Motor('C')
c_sensor = ColorSensor('E')
d_sensor = DistanceSensor('D')
motor_pair.set_default_speed(10)

# Write your program here.
hub.speaker.beep()

def OrientateHub():
    # resets robot yaw to 0
    hub.motion_sensor.reset_yaw_angle()

def ScanForBall():
    while True:
        distance = d_sensor.get_distance_cm()
        if distance != None and distance <= 4:
            LiftArm()
        color = c_sensor.get_color()
        # start moving forward
        motor_pair.start()
        if color != 'black':
            continue
        else:
            # stop robot
            motor_pair.stop()
            # while robot is not facing correct angle
            while True:
                yaw = hub.motion_sensor.get_yaw_angle()
                if yaw <= -90:
                    break
                # rotate robot
                motor_pair.start_tank(-10, 10)
            # stop robot
            motor_pair.stop()
            # move forward 10cm
            motor_pair.move(10, 'cm')
            # while robot is not facing correct angle
            while True:
                yaw = hub.motion_sensor.get_yaw_angle()
                if abs(yaw) == 180:
                    break
                # rotate robot
                motor_pair.start_tank(-10, 10)
            # stop robot
            motor_pair.stop()
            

def LiftArm():
    # stop robot
    motor_pair.stop()
    # wait 2 seconds
    wait_for_seconds(2)
    # lift arm 45 degrees
    motor_c.run_for_degrees(-45, 10)
    GoHome()
    

def GoHome():
    while True:
        color = c_sensor.get_color()
        # while robot is not facing correct angle
        while True:
            yaw = hub.motion_sensor.get_yaw_angle()
            print(yaw)
            if yaw <= 90 and yaw > 1:
                break
            # rotate robot
            motor_pair.start_tank(-10, 10)
        # stop robot
        motor_pair.stop()
        # start moving forward
        motor_pair.start()
        if color != 'black':
            # stop robot
            continue
        else:
            # while robot is not facing correct angle
            while hub.motion_sensor.get_yaw_angle() != 180:
                # rotate robot
                motor_pair.start_tank(-10, 10)
            # stop robot
            motor_pair.stop()
            # start moving forward
            motor_pair.start()
            if color == 'black':
                # stop robot
                motor_pair.stop()
            hub.speaker.play_sound('Warp Speed')


def main():
    OrientateHub()
    ScanForBall()

main()