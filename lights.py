import RPi.GPIO as GPIO
from time import sleep
led = 17
button1 = 25
button2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while (True):
	if (GPIO.input(button1) == GPIO.HIGH and GPIO.input(button2) == GPIO.HIGH):
	    GPIO.output(led, GPIO.HIGH)
    else:
	    GPIO.output(led, GPIO.LOW)
        sleep(0.1)
