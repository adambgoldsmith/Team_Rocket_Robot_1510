from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor
from mindstorms.control import wait_for_seconds, Timer
# Create your objects here.

hub = MSHub()
motor_pair = MotorPair('A', 'B')
motor_c = Motor('C')
c_sensor = ColorSensor('E')
d_sensor = DistanceSensor('F')
timer = Timer()

def main():
    hub.speaker.beep()
    motor_pair.set_default_speed(20)
    reorientate()
    Scan()

def reorientate():
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() in range(-175, 175):
        print(hub.motion_sensor.get_yaw_angle())
        motor_pair.start_tank(10, -10)
    motor_pair.stop()

def Scan():
    hub.motion_sensor.reset_yaw_angle()
    timer.reset()
    while True:
        distance = d_sensor.get_distance_cm()
        if c_sensor.get_color() == 'white' or c_sensor.get_color() == 'black':
            motor_pair.stop()
            motor_pair.move(timer.now(), 'seconds', 0, -20)
            Rotate()
            timer.reset()
        else:
            motor_pair.start()
        if distance is not None and distance <= 8:
            final_time = timer.now()
            LiftArm()
            motor_pair.move(final_time, 'seconds', 0, -20)
            break
    Finish()

def Rotate():
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() < 20:
        motor_pair.start_tank(10, -10)
    motor_pair.stop()

def LiftArm():
    motor_pair.stop()
    wait_for_seconds(2)
    motor_c.run_for_degrees(75, 20)

def Finish():
    motor_pair.stop()
    hub.speaker.play_sound("Ha Ha Ha")

main()