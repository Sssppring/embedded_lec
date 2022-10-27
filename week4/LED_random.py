import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD) # BOARD 모드로 설정

GPIO.setup(37, GPIO.OUT) # 각 LED에 해당하는
GPIO.setup(36, GPIO.OUT) # pin번호를 출력으로 설정
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

pins = [37, 36, 40, 38] # 시계방향으로 배열에 추가
idx = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1] # 10번 반복할 수 있도록 배열 선언

random.shuffle(pins) # 무작위 출력을 위해 섞기

try:
    for i in pins: # 모든 LED 초기화
        GPIO.output(i, GPIO.LOW)
    
    for j in idx: # index 순서대로 가져오기
        GPIO.output(pins[j], GPIO.HIGH) # 섞인 배열에서 순서대로 LED ON
        time.sleep(0.5) # 0.5초 대기
        GPIO.output(pins[j], GPIO.LOW) # 섞인 배열에서 순서대로 LED OFF
        time.sleep(0.5) # 0.5초 대기
    GPIO.cleanup()
except:
    GPIO.cleanup()