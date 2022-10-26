import RPi.GPIO as GPIO
import time

PWML = 18
LIN1 = 22
LIN2 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(PWML, GPIO.OUT)
GPIO.setup(LIN1, GPIO.OUT)
GPIO.setup(LIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWML, 500)
L_Motor.start(0)

try:
    while True:
        GPIO.output(LIN1, 0)
        GPIO.output(LIN2, 1)
        L_Motor.ChangeDutyCycle(100)
        time.sleep(1.0)

        GPIO.output(LIN1, 0)
        GPIO.output(LIN2, 1)
        L_Motor.ChangeDutyCycle(0)
        time.sleep(1.0)
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
