#Julian Shniter
#Mexico Game
#a game of mexico where the rolling of two die is compared 
#last edited 12/13/2021
from dice import Die

d1=Die()
d2=Die()

#you could do class objects for the players if you wanted but i dont see the need
playerpoints=6
computerpoints=6
def PlayerTurn(die1, die2):
    roll=die1.roll()+die2.roll()
    print("The player rolls a {}".format( roll))
    return roll
def ComputerTurn(die1, die2):
    roll=die1.roll()+die2.roll()
    print("The computer rolls  {}".format( roll))
    return roll
   #i tried to get it to display both dice but it was being very annoying 

while playerpoints>0 or computerpoints>0:
    if ComputerTurn(d1, d2)>PlayerTurn(d1, d2):
        computerpoints-=1
        print("The computer now has {} points".format(computerpoints))
    else:
        playerpoints-=1
        print("The computer now has {} points".format(computerpoints))
    if computerpoints==0:
        print("The computer loses")
    elif playerpoints==0: 
        print("the player looses")
