import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.bcm)
GPIO.setup(17, GPIO.OUT)
while True:
    GPIO.output(17, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(17, GPIO.LOW)
    sleep(0.5)