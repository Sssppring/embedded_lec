import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # BOARD 모드로 설정

GPIO.setup(37, GPIO.OUT) # 각 LED에 해당하는
GPIO.setup(36, GPIO.OUT) # pin번호를 출력으로 설정
GPIO.setup(40, GPIO.OUT) 
GPIO.setup(38, GPIO.OUT)

pins = [37, 36, 40, 38] # 시계방향으로 배열에 추가

try:
    for i in pins: # 모든 LED 초기화
        GPIO.output(i, GPIO.LOW)
    
    while True: 
        for i in pins: # pins에서 하나씩 가져와서 출력
            GPIO.output(i, GPIO.HIGH) # LED ON
            time.sleep(1.0) # 1초동안 대기
            GPIO.output(i, GPIO.LOW) # LED OFF
            time.sleep(1.0) # 1초동안 대기
except: # 예외 처리
    GPIO.cleanup() # GPIO 설정 초기
