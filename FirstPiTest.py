# Count to 10
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

x = 0
while x < 10:
    x +=1
    print(x)

y=0
while y<10:
    y +=1
    GPIO.output(8,GPIO.HIGH)
    sleep(1)
    GPIO.output(8,GPIO.LOW)
    sleep(1)