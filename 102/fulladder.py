import RPi.GPIO as GPIO
from time import sleep

def setGPIO():
    leds =[17,18,27,22,26,12,16,20,21]
    GPIO.setup(leds, GPIO.OUT)
    return leds

def allOn(leds):
    GPIO.output(leds, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)

leds=setGPIO()
allOn(leds)
sleep(10)
GPIO.cleanup()

