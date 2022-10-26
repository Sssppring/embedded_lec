import RPi.GPIO as GPIO
import time

sw1 = 5
sw2 = 6
sw3 = 13
sw4 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(sw1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        sw1Value = GPIO.input(sw1)
        sw2Value = GPIO.input(sw2)
        sw3Value = GPIO.input(sw3)
        sw4Value = GPIO.input(sw4)

        if sw1Value: print('click 1')
        if sw2Value: print('click 2')
        if sw3Value: print('click 3')
        if sw4Value: print('click 4')

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
