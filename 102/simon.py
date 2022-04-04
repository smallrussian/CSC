import RPi.GPIO as GPIO
from time import sleep 
import pygame
import random

pygame.init()

leds=[6,13,19,21]
switches=[20,16,12,26]
ledsequence=[]
score=0

sounds=[pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def addLight():
    while True:
        val=random.randint(0,3)
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val], False)
        sleep(1/4)
        print("Input it yourself\n")
        if GPIO.input(switches[val]==True):
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(.25)
            ledsequence.append(val)
            break
        else:
            print("Try again\n")

def playlights():
    for i in ledsequence:
        GPIO.output(leds[i], True)
        sounds[i].play()
        sleep(1)
        GPIO.output(leds[i], False)
        sleep(.25)
    
try:
    while(True):
        lose=False
        playlights()
        for n in ledsequence:
            if GPIO.input(switches[n]==True):
                GPIO.output(leds[n], True)
                sounds[n].play()
                score+=1
                sleep(1)
                GPIO.output(leds[n], False)
                sleep(.25)
            else:
                GPIO.output(leds, True)
                sleep(1)
                GPIO.output(leds, False)



except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nbye")

        

#print("Press the switches or Ctrl+C to exit...")
#try:
    #while (True):
       # pressed=False
        #while(not pressed):
         #   for i in range(len(switches)):
          #      while(GPIO.input(switches[i])==True):
           #         val=i
                    
            #        pressed=True
        #do light and sound
        #GPIO.output(leds[val], True)
        #sounds[val].play()
        #sleep(1)
        #GPIO.output(leds[val], False)
        #sleep(0.25)
#except KeyboardInterrupt:
    #GPIO.cleanup()
    #print("\nBye!")
