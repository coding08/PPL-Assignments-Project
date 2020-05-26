from animals import *
from shapes import *


lion = Lion('20 years')
lion.setsound('Roaring')
lion.typeOfAnimal()
print(lion.getsound())
print(lion.is_living)
lion.eats()
print(lion.get_lifespan())
print('\n')

saber = SaberTooth('30 years')
saber.is_extinct()
saber.eats()
print(saber.legs)

sq = Square()
rec = Rectangle()
tri = Triangle()
pen = Pentagon()
cir = Circle()
hexa = Hexagon()
cube = Cube()
cuboid = Cuboid()
cone = Cone()
prl = Parallelogram()
