import RPi.GPIO as GPIO
import time

buzzer = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)

p = GPIO.PWM(buzzer, 261)
p.start(50)

try:
    while True:
        p.start()
        p.ChangeFrequency(261)
        time.sleep(1.0)
        p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
