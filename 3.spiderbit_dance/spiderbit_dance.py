from microbit import i2c, sleep, button_a
import motor

Motor = motor.DCMotors(i2c)

if button_a.is_pressed():
    while True:
        Motor.MotorRun(1, 120)
        Motor.MotorRun(3, 120)
        sleep(2000)
        Motor.MotorRun(1, 255)
        Motor.MotorRun(3, -255)
        sleep(2000)
        Motor.MotorRun(1, -120)
        Motor.MotorRun(3, 120)
        sleep(4000)
        Motor.MotorRun(1, -255)
        Motor.MotorRun(3, -255)
        sleep(2000)
