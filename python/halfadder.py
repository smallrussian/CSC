import RPi.GPIO as GPIO
from time import sleep

#set the GPIO pin numbers
inA=25
inB=5
outS=17
outC=22

#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup the input and output pins
GPIO.setup(inA. GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outS, GPIO.OUT)
GPIO.setup(outC, GPIO.OUT)

try:
    #keep going until the user presses CTRL+C
    while (True):
        A=0
        B=0
        S=0
        C=0
        # set A and B depending on the switches
        A = GPIO.input(inA)
        B = GPIO.input(inB)
        # calculate S and C depending on A and B
        S = A ^ B # A xor B
        C = A & B # A and B
        # set the output pins appropriately
        # (to light the LEDs as appropriate)
        GPIO.output(outS, S)
        GPIO.output(outC, C)
#detect CTRL+C
except:
    #reset the GPIO pins
    GPIO.cleanup()
