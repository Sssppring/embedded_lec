import RPi.GPIO as GPIO
import time

PWML = 18
LIN1 = 22
LIN2 = 27

PWMR = 23
RIN1 = 25
RIN2 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(PWML, GPIO.OUT)
GPIO.setup(LIN1, GPIO.OUT)
GPIO.setup(LIN2, GPIO.OUT)
GPIO.setup(PWMR, GPIO.OUT)
GPIO.setup(RIN1, GPIO.OUT)
GPIO.setup(RIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWML, 500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMR, 500)
R_Motor.start(0)

try:
    while True:
        GPIO.output(RIN1, 0)
        GPIO.output(RIN2, 1)
        R_Motor.ChangeDutyCycle(50)
        time.sleep(1.0)

        GPIO.output(RIN1, 0)
        GPIO.output(RIN2, 1)
        R_Motor.ChangeDutyCycle(0)
        time.sleep(1.0)
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
