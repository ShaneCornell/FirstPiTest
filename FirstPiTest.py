# Count to 10
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
# print("Start")
# y=0
# while y<100:
#     y +=1
#     GPIO.output(8,GPIO.HIGH)
#     sleep(1)
#     print(y)
#     GPIO.output(8,GPIO.LOW)
#     sleep(1)

from gpiozero import Servo
from time import sleep

servo = Servo(8)
while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)