from tkinter import *
import math
from random import choice, randint, sample


#i made these but did not need them
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
    
    #initializes our vertex vector 
    verticies=[]
    
    #https://www.codegrepper.com/code-examples/python/tkinter+draw+a+dot
    def create_circle(self, x, y, r, color):
        x0=x-r
        y0=y-r
        x1=x+r
        y1=y+r
        return self.create_oval(x0, y0, x1, y1, outline=color, fill=color)


    #plots the point 
    def plotPoint(self, point, radius, color):
        #self.create_line(point._x, point._y, point._x+1, point,_y, fill=color)
        self.create_oval(point._x, point._y, point._x, point._y, fill=color, outline=color, width=radius)

    #function for verticies
    #i tried using overloading instead of a different function and it went from working to really messed
    def plotVertex(self, point, radius, color):
        self.create_circle(point._x, point._y, radius, color)
        self.verticies.append(point)

    #chaos engine
    def chaos(self):
        v1,v2=sample(self.verticies, 2)
        midpt=v1.midpt(v2)
        self.plotPoint(midpt, 1.5, "blue")
        for i in range(15000):
            v=choice(self.verticies)
            m=midpt.midpt(v)
            self.plotPoint(m, 1.5, "blue")
            midpt=m
        
        


   


    

#mainloop
root=Tk()
root.title("Chaos Game")
c=ChaosGame(root, height=600, width=520, bg='violet')
#plot the verticies 
c.plotVertex(Point(255,20), 4, "red")
c.plotVertex(Point(5, 595), 4, "red")
c.plotVertex(Point(515, 595), 4, "red")
#i went a step further and made a button 
b=Button(root, text="Make\nChaos?", command=lambda: [c.chaos(), b.place_forget()])
b.place(x=235,y=400)

#c.plotVertex(Point(260, 400), 5, "blue")
c.pack()

root.mainloop()