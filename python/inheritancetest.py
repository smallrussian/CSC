import abc

class Shape(metaclass=abc.ABCMeta):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    
    @abc.abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        return(.5*self.base*self.height)
        
class Parollelogram(Shape):
    def area(self):
        return(self.base*self.height)

class Trapezoid(Shape):
    def __init__(self, base, height, base2):
        super().__init__(base, height)
        self.base2=base2
    def area(self):
        return(.5*self.height*(self.base+self.base2))

triangle=Triangle(2, 3)
parolellogram=Parollelogram(2,3)
trapezoid=Trapezoid(2,3,3)

print(triangle.area())
print(parolellogram.area())
print(trapezoid.area())

    
