from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor
from mindstorms.control import wait_for_seconds, Timer

# Create your objects here.
hub = MSHub()
motor_pair = MotorPair('A', 'B')
motor_c = Motor('C')
c_sensor = ColorSensor('E')
d_sensor = DistanceSensor('D')
timer = Timer()

def main():
    hub.speaker.beep()
    motor_pair.set_default_speed(10)
    Scan()

def Scan():
    hub.motion_sensor.reset_yaw_angle()
    distance = d_sensor.get_distance_cm()
    timer.reset()
    while True:
        if c_sensor.get_color() == 'black':
            motor_pair.stop()
            motor_pair.move(timer.now(), 'seconds', 0, -10)
            Rotate()
        else:
            motor_pair.start()
        if distance is not None and distance <= 4:
            final_time = timer.now()
            LiftArm()
            motor_pair.move(final_time, 'seconds', 0, -10)
            break
    Finish()

def Rotate():
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() < 15:
        motor_pair.start_tank(10, -10)
    motor_pair.stop()
    timer.reset()

def LiftArm():
    motor_pair.stop()
    wait_for_seconds(2)
    motor_c.run_for_degrees(-45, 10)

def Finish():
    motor_pair.stop()
    hub.speaker.play_sound("Ha Ha Ha")

main()
