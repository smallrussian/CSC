import RPi.GPIO as GPIO
from time import sleep 
import pygame

pygame.init()

leds=[6,13,19,21]
switches=[20,16,12,26]

sounds=[pygame.mixer.Sound("one.wav"),
pygame.mixer.Sound("two.wav"),
pygame.mixer.Sound("three.wav"),
pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Press the switches or Ctrl+C to exit...")
try:
    while (True):
        pressed=False
        while(not pressed):
            for i in range(len(switches)):
                while(GPIO.input(switches[i])==True):
                    val=i
                    pressed=True
        #do light and sound
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val], False)
        sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye!")
