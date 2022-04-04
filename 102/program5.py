class Shape:
    
    def __init__(self, height=1, width=1):
        self.height = height
        self.width = width
    
    def __str__(self):
        for i in range(self.width):
            shape = ("* " * self.height)
        return shape
    
    def setHeight(self, value):
        self.height=value

    def getHeight(self):
        return self.height
    
    def setWidth(self, value):
        self.width=value
    
    def getWidth(self):
        return self.width


class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__(l, w)

class Square(Shape):

    def __init__(self, l):
        super().__init__(l, l)

class Parollelogram(Shape):
    def __init__(self, height=1, width=1):
        super().__init__(height, width)
    
    #https://stackoverflow.com/questions/47500668/how-to-draw-a-parallelogram-with-characters-in-python
    def __str__(self):
        shape=""
        for i in range(1, self.height+1):
            tempshape=' ' * (self.height+1-i) + '* ' * self.width + ' ' * i+'\n'
            shape=shape+tempshape

        return shape

p=Parollelogram(5,10)
print(p)