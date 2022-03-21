from tkinter import *
import math
from random import choice, randint
HEIGHT=600
WIDTH=520
MIN_X=3
MIN_Y=3

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x=x
        self._y=y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x=value
    
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y=value
    
    ##methods
    def dist(self, p2):
        dist=math.sqrt(((self._x-p2._x)**2 +(self._y-p2._y)**2))
        return dist

    def midpt(self, p2):
        point1=((self._x+p2._x)/2)
        point2=((self._y+p2._y)/2)
        return Point(point1, point2)
    
    def __str__(self) -> str:
        return "({},{})".format(self._x, self._y)

class CoordinateSystem(Canvas):
    colors= ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    pointradius=0
    
    def plot(self, point, color):
        #https://stackoverflow.com/questions/30168896/tkinter-draw-one-pixel
        self.create_rectangle((point._x, point._y)*2, outline=color, fill=color)    
   
    def plotPoints(self, plotnum=50000):
        for i in range(plotnum):
            self.plot(Point(randint(0,HEIGHT), randint(0,WIDTH)), choice(self.colors))
    #p
    def plotVertex(self):
        self.plot(Point(522,3), color="red")


#mainloop
root=Tk()
c=CoordinateSystem(root, height=600, width=520)
c.plotVertex()
c.pack()
root.mainloop()