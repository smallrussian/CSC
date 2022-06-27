import sys, random

class Die:
    def __int__(self, sides):
        self.sides=sides
    def roll(self):
        r=random.randint(1, self.sides)
        return(r)