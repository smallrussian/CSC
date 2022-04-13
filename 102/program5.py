


class Shape:
    
    def __init__(self, height=1, width=1):
        self.height = height
        self.width = width
        if(self.height<=0):
            self.height=1
        if(self.width<=0):
            self.width=1

    
    def __str__(self):
        shape=""
        for i in range(self.width):
            tempshape = ("* " * self.height)+'\n'
            shape=shape+tempshape
        return shape
    
    #i mean i guess you could use them for range checking
    #but also its two values why not do it in __init__
    #but i understand why gourd wants us to do it 
    def setHeight(self, value):
        self.height=value

    def getHeight(self):
        return self.height
    
    def setWidth(self, value):
        self.width=value
    
    def getWidth(self):
        return self.width


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

class Square(Shape):

    def __init__(self, height):
        super().__init__(height, height)

class Triangle(Shape):
    def __init__(self, height):
        super().__init__(height, height)
    
    def __str__(self):
        shape=""
        for i in range(self.width):
            tempshape=("* "*(self.width-i)+'\n')
            shape=shape+tempshape
        return shape

class Parollelogram(Shape):
    def __init__(self, height=1, width=1):
        super().__init__(height, width)
    
    #https://stackoverflow.com/questions/47500668/how-to-draw-a-parallelogram-with-characters-in-python
    def __str__(self):
        shape=""
        for i in range(1, self.height+1):
            tempshape=" " * (self.height+1-i) + "* " * self.width + " " * i+"\n"
            shape=shape+tempshape
        return shape


        

#int main()
r1=Rectangle(12,4)
print(r1)
s1=Square(5)
print(s1)
t1=Triangle(7)
print(t1)
p1=Parollelogram(3,10)
print(p1)
r2=Rectangle(0,0)
print(r2)
p1.width=2
p1.width=-1
p1.height=2 #the instructions call for accessors and mutators but doesnt even put them here where it would be appropriate
#maybe im just wrong and confused alltogether tho
print(p1)
#ok back to SciFiLi