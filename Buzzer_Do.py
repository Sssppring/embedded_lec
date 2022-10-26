import RPi.GPIO as GPIO
import time

buzzer = 12

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)

p = GPIO.PWM(buzzer, 261)
p.start(50)

tone = [261, 293, 329, 349, 391, 440, 494, 523]

try:
    for i in tone:
        p.ChangeFrequency(i)
        time.sleep(0.5)
    p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
