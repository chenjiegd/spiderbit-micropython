from microbit import sleep, i2c
import motor

Motor = motor.DCMotors(i2c)
Motor.MotorRun(1, 255)
Motor.MotorRun(3, 255)
sleep(1000)
Motor.MotorStopAll()
