from abc import ABC, abstractmethod 
import math
import time

class Shapes(ABC):

    def __init__(self):
        self.geometrical = True
    
    @abstractmethod
    def type(self):
        pass


class Calculate(ABC):                 # Interface Class

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

        
class Square(Shapes, Calculate):

    def __init__(self,s=100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def getside(self):
        return self.s
    
    def setside(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

    def perimeter(self):
        return 4 * self.s

class Rectangle(Shapes, Calculate):
    
    def __init__(self, l=200, b=100):
        Shapes.__init__(self)
        self.l = l
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def getter(self):
        return self.l, self.b

    def setter(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

class Triangle(Shapes, Calculate):
    
    def __init__(self, a = 100, b = 100, c = 100):
        Shapes.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def type(self):
        print("It is a 2-D shape")

    def getsides(self):
        return self.a, self.b,self.c


    def setsides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.s) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return (self.a + self.b + self.c)


class Pentagon(Shapes, Calculate):

    def __init__(self, s = 100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s
    
    def getside(self):
        return self.s

    def area(self):
        return ((s**2 / 4) * (math.sqrt(5 * (5 + (2*math.sqrt(5))))))

    def perimeter(self):
        return 5 * self.s

class Circle(Shapes, Calculate):
    
    def __init__(self, r = 100):
        Shapes.__init__(self)
        self.r = r

    def type(self):
        print("It is a 2-D shape")

    def setradius(self,r):
        self.r = r

    def getradius(self):
        return self.r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

class Hexagon(Shapes, Calculate):

    def __init__(self, s = 100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s

    def getside(self):
        return self.s

    def area(self):
        return (1.5 * math.sqrt(3) * (a**2))

    def perimeter(self):
        return 6 * self.s

class Parallelogram(Shapes, Calculate):

    def __init__(self, a = 100, b = 200):
        Shapes.__init__(self)
        self.a = a
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def setter(self, a, b):
        self.a = a
        self.b = b

    def getter(self):
        return self.a, self.b

    def area(self):
        return (b * (a * math.sin(45 * (math.pi / 180))))

    def perimeter(self):
        return 2 * (a + b)

class Cube(Shapes, Calculate):

    def __init__(self, s = 200):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 3-D shape")

    def setside(self, s):
        self.s = s
    
    def getside(self):
        return self.s

    def area(self):
        return 6 * (self.s**2)

    def perimeter(self):
        print("Cannot be calculated")

    def volume(self):
        return self.s**3

class Cuboid(Shapes, Calculate):

    def __init__(self, l = 200, b = 100, h = 50):
        Shapes.__init__(self)
        self.l = l
        self.b = b
        self.h = h

    def type(self):
        print("It is a 3-D shape")

    def setter(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h
    
    def getside(self):
        return self.l, self.b, self.h

    def area(self):
        return 2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))

    def perimeter(self):
        print("Cannot be calculated")

    def volume(self):
        return self.l * self.b * self.h

class Cone(Shapes, Calculate):

    def __init__(self):
        Shapes.__init__(self)
        self.angle = 45
        self.side = 200

    def type(self):
        print("It is a 3-D shape")

    def area(self):
        print("Not Calculated")

    def perimeter(self):
        print("Not calculated")