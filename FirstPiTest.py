# Count to 10
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
print("Start")
y=0
while y<100:
    y +=1
    GPIO.output(8,GPIO.HIGH)
    sleep(1)
    print(y)
    GPIO.output(8,GPIO.LOW)
    sleep(1)