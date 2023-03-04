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

# Write your program here.

def OrientateHub():
    # resets robot yaw to 0
    hub.motion_sensor.reset_yaw_angle()

def ScanForBall():
    distance = d_sensor.get_distance_cm()
    direction = True
    while True:
        if distance is not None and distance <= 4:
            LiftArm()
            break
        if c_sensor.get_color() == 'black':
            motor_pair.stop()
            if direction == True:
                while hub.motion_sensor.get_yaw_angle() > -90:
                    motor_pair.start_tank(-10, 10)
                motor_pair.stop()
                motor_pair.move(10, 'cm')
                while hub.motion_sensor.get_yaw_angle() < 0:
                    motor_pair.start_tank(-10, 10)
                motor_pair.stop()
                direction = False
            else:
                while hub.motion_sensor.get_yaw_angle() != -90:
                    motor_pair.start_tank(10, -10)
                motor_pair.stop()
                motor_pair.move(10, 'cm')
                while hub.motion_sensor.get_yaw_angle() != 0:
                    motor_pair.start_tank(10, -10)
                motor_pair.stop()
                direction = True
        else:
            motor_pair.start()

def LiftArm():
    motor_pair.stop()
    wait_for_seconds(2)
    motor_c.run_for_degrees(-45, 10)
    GoHome()

def GoHome():
    while hub.motion_sensor.get_yaw_angle() != 90:
        motor_pair.start_tank(-10, 10)
    motor_pair.stop()
    motor_pair.start()
    while True:
        if c_sensor.get_color() == 'black':
            motor_pair.stop()
            while hub.motion_sensor.get_yaw_angle() in range(-175, 175):
                motor_pair.start_tank(-10, 10)
            motor_pair.stop()
            motor_pair.start()
            while True:
                if c_sensor.get_color() == 'black':
                    Finish()
                    break
            break


def Finish():
    motor_pair.stop()
    hub.speaker.play_sound("Ha Ha Ha")

def main():
    hub.speaker.beep()
    motor_pair.set_default_speed(10)
    OrientateHub()
    ScanForBall()

main()