from distutils.version import LooseVersion
import RPi.GPIO as GPIO
from time import sleep 
import pygame
import random
from Debug import DEBUG
pygame.init()

leds=[6,13,19,21]
switches=[20,16,12,26]
ledsequence=[]
score=0
multiplier=1
lightidentifier=True
global lose
lose=False
sounds=[pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def addLightinitial():
    pressed=False
    val=random.randint(0,3)
    while True:
        GPIO.output(leds[val], True)
        sounds[val].play()
        (1)
        GPIO.output(leds[val], False)
        (1/4)
        print("Input it yourself\n")
        while not pressed:
            for i in range(len(switches)):
                while(GPIO.input(switches[i])==True):
                    tempval=i
                    pressed=True
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val], False)
        sleep(.25)
        if tempval==val:
            ledsequence.append(val)
            break 

        else:
            print("Try again and select the correct light\n")
            pressed=False
            continue

def addLight():
    val=random.randint(0,3)
    ledsequence.append(val)
    if DEBUG==True:
        print("light added")

def playlights():
    if DEBUG==True:
        colorsequence=[]
        for j in ledsequence:
            if j==0:
                colorsequence.append("red")
            elif j==1:
                colorsequence.append("blue")
            elif j==2:
                colorsequence.append("yellow")
            elif j==3:
                colorsequence.append("green")
        print(colorsequence)

    for i in ledsequence:
        sounds[i].play()
        if lightidentifier==True:
            GPIO.output(leds[i], True)
            sleep(1*multiplier)
            GPIO.output(leds[i], False)
            sleep(.25*multiplier)
    
def inputSequence():
    for i in range(len(ledsequence)):
        pressed=False
        while not pressed:
            for n in range(len(switches)):
                while (GPIO.input(switches[n])==True):
                    val=n
                    pressed=True
        sounds[val].play()
        if lightidentifier==True:
            GPIO.output(leds[val], True)
            sleep(1*multiplier)
            GPIO.output(leds[val], False)
            sleep(.25*multiplier)
        if val==ledsequence[i]:
            print ("Good job")
            continue
        else:
            return False
    return True   

def loss():
    for i in range(3):
        GPIO.output(leds[0], True)
        GPIO.output(leds[1], True)
        GPIO.output(leds[2], True)
        GPIO.output(leds[3], True)
        sleep(1)        
        GPIO.output(leds[0], False)
        GPIO.output(leds[1], False)
        GPIO.output(leds[2], False)
        GPIO.output(leds[3], False)
        sleep(.25)


    

                    

    
try:
    addLightinitial()
    turncounter=0
    while lose==False:
        while turncounter>=5:
            multiplier=+.1
        if turncounter==15:
            lightidentifier=False


        addLight()
        playlights()
        if inputSequence()==False:
            lose=True
        else:
            score=+1
            turncounter=+1
        
    if lose==True:
        loss()
        print("ha ha you suck")
    print("thanks for playing. You scored {} points".format(score))
        
        


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
