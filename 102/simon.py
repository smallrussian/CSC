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
    subpressed=False
    val=random.randint(0,3)
    GPIO.output(leds[val], True)
    sounds[val].play()
    sleep(1)
    GPIO.output(leds[val], False)
    sleep(1/4)
    print("Input it yourself\n")
    while True:
        while not subpressed:
            for i in range(len(switches)):
                while(GPIO.input(switches[i])==True):
                    tempval=i
                    subpressed=True

        if tempval==val:
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(.25)
            ledsequence.append(val)
            break
                
                

        else:
            print("Try again and select the correct light\n")
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
        GPIO.output(leds[i], True)
        sounds[i].play()
        sleep(1)
        GPIO.output(leds[i], False)
        sleep(.25)
    
def inputSequence():
    for i in range(len(ledsequence)):
        pressed=False
        while not pressed:
            for n in range(len(switches)):
                while (GPIO.input(switches[n])==True):
                    val=n
                    pressed=True
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val], False)
        sleep(.25)
        if val==ledsequence[i]:
            print ("nice")
            continue
        else:
            print("You lose")
            return False
    return True   

    

                    

    
try:
    addLightinitial()
    while lose==False:
        addLight()
        playlights()
        if inputSequence()==False:
            lose=True
    if lose==True:
        print("ha ha you suck")
    print("thanks for playing")
        
        


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
