#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import threading
import serial
import time

sw = [5, 6, 13, 19] # pin 번호 배열
PWM = [18, 23] # 
Min = [22, 27, 25, 24] # 왼쪽 모터 출력 PWM, IN1, IN2
 # 오른쪽 모터 출력 PWM, IN1, IN2

GPIO.setmode(GPIO.BCM) # GPIO를 BCM 모드로 설정

map(lambda a: GPIO.setup(a, GPIO.IN, pull_up_down = GPIO.PUD_DOWN),sw) # 스위치 세팅
map(lambda a: GPIO.setup(a, GPIO.OUT), PWM) # Motor PWM 핀 세팅
map(lambda a: GPIO.setup(a, GPIO.OUT), Min) # Motor 입력 핀 세팅

last = [0, 0, 0, 0] # 직전 스위치 값 저장 배열
curr = [0, 0, 0, 0] # 현재 스위치 값 저장 배열

# 진행 방향에 따라 입력할 RIN1, RIN2, LIN1, LIN2, Rspeed, Lspeed
GO = [0, 1, 0, 1, 50, 50]
RIGHT = [0, 1, 1, 0, 100, 40]
LEFT = [1, 0, 0, 1, 40, 100]
BACK = [1, 0, 1, 0, 50, 50]
STOP = [0, 1, 0, 1, 0, 0]

R_Motor = GPIO.PWM(PWM[0], 500)
R_Motor.start(0)

L_Motor = GPIO.PWM(PWM[1], 500)
L_Motor.start(0)

# list 입력받아 출력
def PrintMotor(dir):
    print(dir)
    for i in range(4):
        GPIO.output(Min[i], dir[i])
    R_Motor.ChangeDutyCycle(dir[4])
    L_Motor.ChangeDutyCycle(dir[5])

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

def serial_thread():
  global gData
  while True:
    data = bleSerial.readline()
    data = data.decode()
    gData = data

def main():
  global gData
  try:
    while True:
      if gData.find("go") >= 0:
        gData = ""
        PrintMotor(GO)
        print("ok go")
      elif gData.find("back") >= 0:
        gData = ""
        PrintMotor(BACK)
        print("ok back")
      elif gData.find("left") >= 0:
        gData = ""
        PrintMotor(LEFT)
        print("ok left")
      elif gData.find("right") >= 0:
        gData = ""
        PrintMotor(RIGHT)
        print("ok right")
      elif gData.find("stop") >= 0:
        gData = ""
        PrintMotor(STOP)
        print("ok stop")
  
  except KeyboardInterrupt:
    GPIO.cleanup()
    pass

if __name__ == '__main__':
  task1 = threading.Thread(target = serial_thread)
  task1.start()
  main()
  bleSerial.close()


  