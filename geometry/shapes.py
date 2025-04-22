#This is lizzy saldanas geometry calc   
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return self.length*2+self.width*2
    
class Square(Rectangle):#Subclass for squares
    def __init__(self, side):
        super().__init__(side, side)  #A square has equal length and width

    
class Circles:
    def __init__(self, radius):
        self.radius = radius

    
    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return self.radius*2*3.14
    
class Triangle:
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return self.base*self.height/2

    def perimeter(self):
        return self.base+self.side1+self.side2