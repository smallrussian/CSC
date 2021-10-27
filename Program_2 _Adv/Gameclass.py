import math
import random
import sys
pile=random.randint(10,100)
pile=int(pile)
halfpile=pile/2
halfpile=int(halfpile)
randchoice=random.randint(1, halfpile)#randchoice is the halfpile
class Computer:
    def __init__(self, draw):
        self.draw=draw
    def easydraw(self):
        print(self.draw)
        return self.draw
    #def harddraw(self):
        #for i in range(8)




obj=Computer(randchoice)
#obj.easydraw()
print(8*sys.getsizeof(randchoice))
print(randchoice)