#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

sw = [5, 6, 13, 19] # pin 번호 배열
fre = [261, 239, 329, 391] # 스위치 별 출력 주파수

buzzer = 12 # buzzer pin 번호

GPIO.setmode(GPIO.BCM) # GPIO를 BCM 모드로 설정

GPIO.setup(buzzer, GPIO.OUT) # buzzer 세팅
map(lambda a: GPIO.setup(a, GPIO.IN, pull_up_down = GPIO.PUD_DOWN),sw) # 스위치 세팅

p = GPIO.PWM(buzzer, 261)

last = [0, 0, 0, 0] # 직전 스위치 값 저장 배열
curr = [0, 0, 0, 0] # 현재 스위치 값 저장 배열

try:
    while True:
        for i in range(4):
            curr[i] = GPIO.input(sw[i]) # 현재 스위치 값 저장
            if last[i] != curr[i]: # 현재 값과 직전 값을 비교해서
                # 현재 값과 직전값이 다를 때
                if curr[i]: # 0->1 경우에만
                    p.start(50)
                    p.ChangeFrequency(fre[i]) # 해당 주파수 출력
                else: p.stop()
                last[i] = curr[i] # 직전 값을 현재 값으로 update
            

except KeyboardInterrupt:
    pass

GPIO.cleanup()
