#Sieve of Eratosthenes
#Checks the highest possible prime number that is less than a given number
#Last edited: 10/13/2021
#Julian Shniter
from time import perf_counter
import math
import array as arr
class Num():
    def __init__(self, num, isPrime=True):
        self.num=num
        self.isPrime=isPrime
    
    def getValue(self):
        return self.num

    def checkIfPrime(self):
        return self.isPrime

    def changeIsPrime(self):
        self.isPrime=not(self.isPrime)
        return self.isPrime



#i found the psuedocode on wikipedia https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
#then i coded based off the psuedocode
#only to realize i did the same thing as this https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def sieve(num, checkprime, changeprime):
    start=perf_counter()
    primearray =[checkprime for i in range(num+1)]

    n=2
    while n*n<=num: #i had for n in range(2, int(math.sqrt(num)))
        #but google said to do ty
        if primearray[n]==True:
            for i in range(n**2, num+1, n):
                primearray[i]=changeprime
        n+=1
    primearray[0]=changeprime
    primearray[1]=changeprime
    primelist=arr.array('i', [])
    for n in range(num+1):
        if primearray[n]==True:
            primelist.append(n)
    print("The highest prime number less than {} is {}".format(num, max(primelist)))
    end=perf_counter()
    comp_time=(end-start)
    #print(comp_time)
    print("It took {} seconds to calculate this".format(comp_time))
#mainloop

print("Welcome to the Sieve of Eratosthenes")
while True:
    usrinput=int(input("Please enter a number between 1 and 100...\n"))
    if usrinput<1 or usrinput>100:
        print("You did not enter a valid number.\nPlease try again.")
    else:
        break
number=Num(usrinput)
sieve(number.getValue(), number.checkIfPrime(), number.changeIsPrime())
