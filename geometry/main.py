import math

class Shape:
    def __init__(self, side):
        self.side = side


    def paramenter(self):
        return self.side*4
    
shape = Shape(8)
print(shape.paramenter()) 

class Sqaure:
    def __init__(self, side):
        self.side = side
    
    def area(self, side):
        return side*side

    def perimeter(self, side):
        return side*4
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self, length, width):
        return length*width

    def perimeter(self, length, width):
        return length*2+width*2
    
class Circles:
    def __init__(self, radius):
        self.radius = radius

    
    def area(self, radius):
        return radius**2*math.pi

    def perimeter(self, radius):
        return radius*2*math.pi
    
class Triange:
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self, base, height):
        return base*height/2

    def perimeter(self, base, side1, side2):
        return base+side1+side2