#Marble Game
#simulates a game where you draw marbles from a pile vs a computer
#rules explained further down in the program
#Last Edited: 10/9/2021
#Julian Shniter


import random
import sys

def pilesize():
    pile=int(random.randint(10,100))
    return pile
globalpile=pilesize()
halfpile=int(globalpile/2)

def randchoice(pile):
    if pile==1:
        return 1
    else:
        randchoice=random.randint(1,pile)
        return randchoice

def highestPowerof2(n): #credit to these guys https://www.geeksforgeeks.org/highest-power-2-less-equal-given-number/
	if (n < 1):
		return 0
	res = 1
	for i in range(8*sys.getsizeof(n)):
		curr = 1 << i
		if (curr > n):
			break
		res = curr
	return res

class Computer:
    def __init__(self):
        pass

    def easydraw(self,pile, hpile):
        if pile==1:
            hpile=pile
        easydraw=randchoice(hpile)
        return easydraw

    def harddraw(self, pile, hpile):
        if pile==1:
            return 1
        try:
            #print(highestPowerof2(randchoice())-1)
            answer = (highestPowerof2(hpile)-1)
        except highestPowerof2(hpile)==0:
            answer=randchoice()
        return answer

class Player:
    def __init__(self, name):
        self.name=name
    def drawmarbles(self, pile, hpile):
        pchoice=0
        if pile==1:
            hpile=pile
        try:
            pchoice=int(input("{}, pick a number between 1 and {}\n".format(self.name,hpile)))
        #print(pchoice)
        except pchoice>hpile:
            print("You selected an invalid number")
        else:
            return pchoice

#these should be the same except the computer is calling its hard draw
def easygame(pile, playerone, playertwo):
    comp=Computer()
    p1=Player(playerone)
    p2=Player(playertwo)
    compplayer="Computer"
    currentplayer=""
    print("The pile has {} marbles".format(pile))
    print("{}, you get to go first".format(playerone))
    while pile>0: #i tried to get it to know when the pile hit zero but it kept breaking
        pile-=p1.drawmarbles(pile, pile//2)
        print("The pile now has {} marbles".format(pile))
        pile-=p2.drawmarbles(pile, pile//2)
        print("The pile now has {} marbles".format(pile))
        compchoice=comp.easydraw(pile, pile//2)
        print("The computer selects {} marbles from the pile".format(compchoice))
        pile-=compchoice
        print("The pile now has {} marbles".format(pile))
        currentplayer="Computer"
        if pile==0:
            if currentplayer==playerone:
                print("{} loses :(")
                break#the break is messy but it gets the job done
            elif currentplayer==playertwo:
                print("{} loses :(")
                break
            elif currentplayer=="Computer":
                print("The computer loses :)")
                break


#this got copied and pasted except for line 
def hardgame(pile, playerone, playertwo):
    comp=Computer()
    p1=Player(playerone)
    p2=Player(playertwo)
    compplayer="Computer"
    currentplayer=""
    print("The pile has {} marbles".format(pile))
    print("{}, you get to go first".format(playerone))
    while pile>0: #i tried to get it to know when the pile hit zero but it kept breaking
        pile-=p1.drawmarbles(pile, pile//2)
        print("The pile now has {} marbles".format(pile))
        pile-=p2.drawmarbles(pile, pile//2)
        print("The pile now has {} marbles".format(pile))
        compchoice=comp.harddraw(pile, pile//2)
        print("The computer selects {} marbles from the pile".format(compchoice))
        pile-=compchoice
        print("The pile now has {} marbles".format(pile))
        currentplayer="Computer"
        if pile==0:
            if currentplayer==playerone:
                print("{} loses :(")
                break#the break is messy but it gets the job done
            elif currentplayer==playertwo:
                print("{} loses :(")
                break
            elif currentplayer=="Computer":
                print("The computer loses :)")
                break



#mainloop
print("Welcome to the marble game")
player1=str(input("Player 1, please enter your name...\n"))
player2=str(input("Player 2, please enter your name...\n"))
tuple=player1, player2
whofirst=random.choice(tuple)
#print(whofirst)
if whofirst==player1:
    firstplayer=player1
    secondplayer=player2
else:
    firstplayer=player2
    secondplayer=player1
print("Here are the rules of the game:\n Each player chooses a number of marbles between 1 and half the pile\n The computer does the same. \n whoever draws the last marble looses")
gamechoice=""
while True:
    try:
        gamechoice=str(input('Please type "easy" for the easy game and "hard" for the hard game.\nUse lowercase letters.\n'))
    except gamechoice!="easy" or gamechoice!="hard":
        print("Please choose correctly")

    else:
        if gamechoice=="easy":
            print('you got it')
            easygame(globalpile,firstplayer, secondplayer)
        elif gamechoice=="hard":
            print("nice job ")
            hardgame(globalpile, firstplayer, secondplayer)
            break


