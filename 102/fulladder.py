import RPi.GPIO as GPIO
from time import sleep
from random import randint

def setGPIO():
    leds =[17,18,27,22,26,12,16,20,21]
    GPIO.setup(leds, GPIO.OUT)
    return leds

#def allOn(leds):
    GPIO.output(leds, GPIO.HIGH)

#GPIO.setmode(GPIO.BCM)

#leds=setGPIO()
#allOn(leds)
#sleep(10)
#GPIO.cleanup()

#function that randomly generates an 8-bit binary number
def getNum():
    #create an empty list to represent the bits
    num=[]
    #generate eight random bits
    for i in range(0,8):
        #append a random bit (0 or 1) to the end of the list
        num.append(randint(0,1))
    return num

#displays the sum (by turning on the appropriate LEDS)
def display(num, leds):
    for i in range(len(num)):
        #if the i-th bit is 1, then turn the i-th LED on
        if (num[i]==1):
            GPIO.output(leds[i], GPIO.HIGH)
        #otherwise turn it off
        else:
            GPIO.output(leds[i], GPIO.LOW)

#function that implements a full adder using two half adders
#inputs are Cin, A, and B; coutputs are S and cout
#this is the function that you need to implement
def halfAdder(A, B):
    return(A^B), (A&B)

def fullAdder(cin, A, B):
    s1, c1=halfAdder(A,B)
    s2, c2=halfAdder(s1, cin)
    S=s2
    cout=c1 or c2
    return S, cout

def calculate(num1, num2):
    cout=0
    the_sum=[]
    n=len(num1)-1
    while(n>-0):
        A=num1[n]
        B=num2[n]
        #set the Cin (as the previous half adder's Cout)
        cin=cout
        S, cout=fullAdder(cin, A, B)
        the_sum.inset(0,S)
        n-=1
    the_sum.insert(0, cout)
    return the_sum

GPIO.setmode(GPIO.BCM)
leds=setGPIO()

#get two random numbers and display them to the console
num1=getNum()
num2=getNum()

print("     {}".format(num1))
print("+    {}".format(num2))
print("---------------------------------")

the_sum=calculate(num1, num2)
print("= {}".format(the_sum))

display(the_sum, leds)

input("Press ENTER to terminate")
GPIO.cleanup()
