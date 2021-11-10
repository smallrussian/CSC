import RPi.GPIO as GPIO
from time import sleep, time
#constatns
DEBUG=False
#set the pi to the broadcom pin layout
GPIO.setmode(GPIO.BCM)
#GPIO pins
Trig=18#the sensors trig pin
Echo=27#the sensors echo pin
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)