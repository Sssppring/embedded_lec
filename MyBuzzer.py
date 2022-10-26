import RPi.GPIO as GPIO
import time

buzzer = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)

p = GPIO.PWM(buzzer, 261)
p.start(50)

tone = [391, 440, 494, 440, 391, 440, 494]

try:
    for i in tone:
        p.ChangeFrequency(i)
        time.sleep(0.1)
    p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
