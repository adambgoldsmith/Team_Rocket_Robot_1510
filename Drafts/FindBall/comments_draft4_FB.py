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
    hub.motion_sensor.reset_yaw_angle() # resets robot yaw to 0

def ScanForBall():
    distance = d_sensor.get_distance_cm()
    direction = True # This variable is True when the robot is moving north, and false when the robot is moving south.
    while True:
        if distance is not None and distance <= 4: # If the robot sees the ball
            LiftArm() # Enter LiftArm function
            break # why is this break statement unreachable? we must get to the end of the call stack.
        if c_sensor.get_color() == 'black': # If the color sensor sees black
            motor_pair.stop() # Stop
            if direction == True: # If the robot is going north
                while hub.motion_sensor.get_yaw_angle() > -90:
                    motor_pair.start_tank(-10, 10) # Rotate the robot until it is facing -90 degrees
                motor_pair.stop()
                motor_pair.move(10, 'cm') # Move forward 10cm
                while hub.motion_sensor.get_yaw_angle() < 0: 
                    motor_pair.start_tank(-10, 10) # Rotate the robot until it is facing 180/-180 degrees (south)
                motor_pair.stop()
                direction = False # Change direction to False (south)
            else: # If the robot is going south
                while hub.motion_sensor.get_yaw_angle() != -90:
                    motor_pair.start_tank(10, -10) # Rotate the robot until it is facing -90 degrees
                motor_pair.stop()
                motor_pair.move(10, 'cm') # Move forward 10cm
                while hub.motion_sensor.get_yaw_angle() != 0:
                    motor_pair.start_tank(10, -10) # Rotate the robot until it is facing 0 degrees (north)
                motor_pair.stop()
                direction = True # Change direction to True (north)
        else: # If the robot does not detect black or does not see the ball
            motor_pair.start() # Move forward

def LiftArm():
    motor_pair.stop() # Stop
    wait_for_seconds(2) # Wait 2 seconds
    motor_c.run_for_degrees(-45, 10) # Lift arm 45 degrees
    GoHome() # Enter GoHome function

def GoHome():
    while hub.motion_sensor.get_yaw_angle() != 90:
        motor_pair.start_tank(-10, 10) # Rotate the robot until it is facing 90 degrees
    motor_pair.stop()
    motor_pair.start() # Move forward 
    while True:
        if c_sensor.get_color() == 'black': # If the color sensor sees black
            motor_pair.stop() # Stop
            while hub.motion_sensor.get_yaw_angle() in range(-175, 175):
                motor_pair.start_tank(-10, 10) # Rotate the robot until it is facing 180/-180 degrees (south)
            motor_pair.stop()
            motor_pair.start() # Move forward
            while True:
                if c_sensor.get_color() == 'black': # If the color sensor sees black
                    Finish() # Enter Finish function


def Finish():
    motor_pair.stop() # Stop
    hub.speaker.play_sound("Ha Ha Ha") # Play victory sound

def main():
    OrientateHub() # Enter the OrientateHub function 
    ScanForBall() # Enter the ScanForBall function

main() # Invokes/Enters the main function (PROGRAM STARTS HERE)