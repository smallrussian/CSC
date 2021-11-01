import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.bcm)
button=25
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True
    GPIO.output(17, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(17, GPIO.LOW)
    sleep(0.5)