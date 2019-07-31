# 在这里写上你的代码 :-)
from microbit import i2c, display
from radio import on, config, receive
import motor

Motor = motor.DCMotors(i2c)

config(power=7, group=1)
on()
def get_message():
    msg = receive()
    display.scroll(str(msg))
    if msg == 'A':
        Motor.MotorRun(1, 255)
        Motor.MotorRun(3, 255)
    elif msg == 'B':
        Motor.MotorRun(1, -255)
        Motor.MotorRun(3, -255)
    elif msg == 'C':
        Motor.MotorRun(1, -255)
        Motor.MotorRun(3, 255)
    elif msg == 'D':
        Motor.MotorRun(1, 255)
        Motor.MotorRun(3, -255)
    elif msg == '0':
        Motor.MotorRun(1, 0)
        Motor.MotorRun(3, 0)

while True:
    get_message()
