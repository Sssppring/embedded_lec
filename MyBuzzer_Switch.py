import RPi.GPIO as GPIO
import time

sw1 = 5
buzzer = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(sw1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

tone = [391, 440, 494, 440, 391, 440, 494]

p = GPIO.PWM(buzzer, 261)
p.start(0)

try:
    while True:
        sw1Value = GPIO.input(sw1)
        p.start(0)
        if sw1Value:
            p.start(50)
            for i in tone:
                p.ChangeFrequency(i)
                time.sleep(0.1)
            p.stop()

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    pass