from microbit import i2c, button_a, button_b
import motor

Motor = motor.DCMotors(i2c)
speed = 50

while True:
    if button_a.is_pressed():
        speed += 50
    elif button_b.is_pressed():
        speed -= 50
    if speed < 0:
        speed = 0
    if speed > 250:
        speed = 250
        
    Motor.MotorRun(1, speed)
    Motor.MotorRun(3, speed)
