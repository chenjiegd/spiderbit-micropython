from microbit import sleep, i2c, button_a, button_b
import PCA9685
import motor

Motor = motor.DCMotors(i2c)
speed = 50

while True:
    if button_a.is_pressed():
        speed += 50
    elif button_b.is_pressed():
        speed -= 50
        
    Motor.MotorRun(1, speed)
    Motor.MotorRun(3, speed)
