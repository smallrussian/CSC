from tkinter import *
import math
from random import choice, randint, sample
from turtle import width


HEIGHT=600
WIDTH=520
MIN_X=6
MIN_Y=6
MAX_X=514
MAX_Y=594

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

class ChaosGame(Canvas):
    verticies=[]
    colors= ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    pointradius=0
    chaoscounter=bool
    
    #https://www.codegrepper.com/code-examples/python/tkinter+draw+a+dot
    def create_circle(self, x, y, r, color):
        x0=x-r
        y0=y-r
        x1=x+r
        y1=y+r
        return self.create_oval(x0, y0, x1, y1, outline=color, fill=color)
        

    def plotPoint(self, point, radius, color):
        #self.create_line(point._x, point._y, point._x+1, point,_y, fill=color)
        self.create_oval(point._x, point._y, point._x, point._y, fill=color, width=radius)

    def plotVertex(self, point, radius, color):
        self.create_circle(point._x, point._y, radius, color)
        self.verticies.append(point)

    def chaos(self):
        v1,v2=sample(self.verticies, 2)
        midpt=v1.midpt(v2)
        self.plotPoint(midpt, 1.5, "black")
        for i in range(15000):
            v=choice(self.verticies)
            m=midpt.midpt(v)
            self.plotPoint(m, 1.5, "black")
            midpt=m
            self.pack()
            self.chaoscounter=True
        


   


    

#mainloop
root=Tk()
root.title("Chaos Game")
c=ChaosGame(root, height=600, width=520)
c.plotVertex(Point(260,10), 3, "red")
c.plotVertex(Point(5, 595), 3, "red")
c.plotVertex(Point(515, 595), 3, "red")
button1=Button(root, text="Make\nChaos?", command=c.chaos)
button1.place(x=260,y=400)
button1.pack_forget()
#c.plotVertex(Point(260, 400), 5, "blue")
c.pack()

root.mainloop()