from abc import ABC, abstractmethod

class Circle(object):
    pi = 3.14

    # Circle get instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius                                   

    # Area method calculates the area. Note the use of self.
    def area(self):
        a = self.radius * self.radius * Circle.pi
        print("Area of circle is {}\n".format(a))

    # Method for resetting Radius
    def setRadius(self, radius):
        self.radius = radius

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius
    
    def noofsides(self):
        print("I am a Circle")
        

C = Circle()
C.noofsides()
C.setRadius(10)
C.area()

class Polygon(ABC):
    def noofsides(self):
        pass

class RegularPolygon(object):
    pi = 3.14

    def __init__(self, side = 1):
        self._side = side

    def area(self):
        print("Area of object is")

    def perimeter(self):
        print("Perimeter of object is")

    def setSide(self, side):
        self._side = side

    def getSide(self):
        return self._side

class Square(RegularPolygon, Polygon):
    def __init__(self, side = 1):
       RegularPolygon.__init__(self, side)

    def area(self):
        RegularPolygon.area(self)
        print(self._side ** 2)
        return self._side**2

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self._side * 4)
        return self._side*4

    def setSide(self, side):
        RegularPolygon.setSide(self,side)

    def getSide(self):
        RegularPolygon.getSide(self)

    def noofsides(self):
        print("I am a Square and I have 4 sides")

S = Square()
S.noofsides()
S.setSide(7)
print(S._side)                                         #Accessing protected member through object is allowed. 
S.perimeter()

class EquilateralTriangle(RegularPolygon, Polygon):
    def __init__(self, side = 1):
       RegularPolygon.__init__(self, side)

    def area(self):
        RegularPolygon.area(self)
        area = ((3**(1/2))/4) * self._side**2
        print(area)
        return area

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self._side * 3)
        return self._side*3

    def setSide(self, side):
        RegularPolygon.setSide(self, side)

    def getSide(self):
        RegularPolygon.getSide(self)

    def noofsides(self):
        print("\nI am an Equilateral Triangle")

E = EquilateralTriangle()
E.noofsides()
E.setSide(10)
E.area()

class Rhombus(Square, Polygon):
    def __init__(self, diagonal1, diagonal2, side = 1):
        RegularPolygon.__init__(self, side)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        RegularPolygon.area(self)
        Area = 1/2 * self.diagonal1* self.diagonal2
        print(Area)
        return Area

    def perimeter(self):
        RegularPolygon.perimeter(self)
        print(self.side * 4)
        return self.side*4

    def set(self, side, diagonal1, diagonal2):
        RegularPolygon.setSide(self)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2


    def get(self):
        RegularPolygon.getSide(self)
        return  self.diagonal1
        return  self.diagonal2

    def noofsides(self):
        print("I have 4 sides")


class Rectangle( Polygon):
   def __init__(self, length = 1, breadth = 1):
        self.length = length
        self.breadth = breadth

   def area(self):
        RegularPolygon.area(self)
        Area = self.length * self.breadth
        print(Area)
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle: ", Perimeter)
        return Perimeter

   def set(self, side1, side2):
        self.length = side1
        self.breadth = side2


   def get(self):
        return self.length
        return self.breadth

   def noofsides(self):
        print("\nI am a Rectangle and I have 4 sides")

R = Rectangle()
R.noofsides()
R.set(10,5)
R.area()

class Parallelogram( Polygon):
   def __init__(self, base = 1, heigth = 1, side = 1):
        self.base = base
        self.heigth = heigth
        self.side = side

   def area(self):
        Area = self.base * self.heigth
        print("Area of parallelogram:", Area)
        return Area

   def perimeter(self):
        Perimeter = 2 * (self.base + self.side)
        print("Perimeter of rectangle: ", Perimeter)
        return Perimeter
   def noofsides(self):
        print("I have 4 sides")

class IsoscelesTriangle(object):
   def __init__(self, side = 1, base = 1, height = 1):
        self.base = base
        self.heigth = heigth
        self.side = side

   def  area(self):
        Area = 1/2 * self.base * self.heigth
        print(Area)
        return Area

   def perimeter(self):
        Perimeter = 2*side + base
        print(Perimeter)
        return Perimeter

class ScaleneTriangle(IsoscelesTriangle):
   def __init__(self, side1 = 1,side2 = 1, base = 1, height = 1):
        self.base = base
        self.heigth = heigth
        self.side1 = side1
        self.side2 = side2

   def  area(self):
        IsoscelesTriangle.area(self)

   def perimeter(self):
        Perimeter = side1 + side2 + base
        print(Perimeter)
        return Perimeter


class Animal(object):
    def __init__(self):
        print ("\nAnimal created")

    def whoAmI(self):
        print ("Animal")

    def eat(self):
        print ("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")

    def whoAmI(self):
        print ("I am a Dog")

    def speaks(self):
        print ("I bark and I am human's Best Friend!")

D = Dog()
D.whoAmI()
D.speaks()

class Cat(Animal):
    def __init__(self):
        Animal.__init__(Self)
        print("Cat created")

    def whoAmI(self):
        print("Cat")

    def speaks(self):
        print("Meow!")

class Panda(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Panada created")

    def whoamI(self) :
        print("Panda")

    def speaks(self):
        print("Squeaking")

class Bear(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Bear created")

    def whoamI(self) :
        print("Bear")

    def speaks(self):
        print("Growl")

class Camel(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Camel created")

    def whoamI(self) :
        print("I am a Camel")

    def speaks(self):
        print("I can store food and water as fat in the hump")

CC = Camel()
CC.whoamI()
CC.speaks()

class Deer(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Deer created")

    def whoamI(self) :
        print("Deer")

    def speaks(self):
        print("Bell")

class Donkey(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Donkey created")

    def whoamI(self) :
        print("Donkey")

    def speaks(self):
        print("Bray")

class Horse(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Horse created")

    def whoamI(self) :
        print("I am a Horse")

    def speaks(self):
        print("I Neigh and I am a Universal Symbol of Freedom without restraint")

H = Horse()
H.whoamI()
H.speaks()

class Jackals(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Jackal created")

    def whoamI(self) :
        print("Jackal")

    def speaks(self):
        print("Howl")

class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Lion created")

    def whoamI(self) :
        print("I am a Lion")

    def speaks(self):
        print("I roar and I am the King of the Jungle")

L = Lion()
L.whoamI()
L.speaks()