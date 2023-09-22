'''
geoshapes.py
A regular polygon class with its variants
'''

import math

class RegularPolygon:
    '''
    Regular polygon class
    '''
    def __init__(self, base, side_number: int):
        self.base = base
        self.side_number = side_number

    def __str__(self) -> str:
        return f"I'm a {self.side_number} sides polygon with {self.base} of base"

    @property
    def apothem(self) -> float:
        '''
        Calculates the apothem of the regular polygon
        '''
        apothem = self.base / (2 * math.tan(math.pi / self.side_number))
        return apothem

    @property
    def area(self) -> float:
        '''
        Calculates the area of a regular polygon
        '''
        return self.apothem * self.perimeter

    @property
    def perimeter(self) -> float:
        '''
        Calculates the perimeter of a regular polygon
        '''
        return self.side_number * self.base

class Triangle(RegularPolygon):
    '''
    Triangle class
    '''
    def __init__(self, base):
        super().__init__(base, 3)

class Square(RegularPolygon):
    '''
    Square class
    '''
    def __init__(self, base):
        super().__init__(base, 4)

class Pentagon(RegularPolygon):
    '''
    Pentagon Class
    '''
    def __init__(self, base):
        super().__init__(base, 5)

class Tetrahedron(Triangle):
    '''
    Tetrahedron class
    '''

    def __str__(self) -> str:
        return f"I'm a tetrahedron with {self.base} of length"

    @property
    def area(self) -> float:
        return 4 * super().area

    @property
    def volume(self) -> float:
        '''
        Calculates the volume of a tetrahedron
        '''
        return math.sqrt(2) / 12 * self.base

class Cube(Square):
    '''
    Cube class
    '''
    def __str__(self) -> str:
        return f"I'm a Cube with {self.base} of length"

    @property
    def area(self) -> float:
        return super().area * 6

    @property
    def volume(self) -> float:
        '''
        Calculates the volume of a cube
        '''
        return self.base ** 3

class Circle():
    '''
    Geometric circle class
    '''
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"I'm a circle with radius = {self.radius}"

    @property
    def diameter(self):
        '''
        Calculates the diameter of the circle
        '''
        return 2 * self.radius

    @property
    def perimeter(self):
        '''
        Calculates the perimeter of the circle
        '''
        return math.pi * self.diameter

    @property
    def area(self):
        '''
        Calculates the area of the circle
        '''
        return math.pi * (self.radius) ** 2

class Cylinder(Circle):
    '''
    Cylinder class
    '''
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def __str__(self):
        return f"I'm a cylinder with radius = {self.radius} and height = {self.height}"

    @property
    def area(self):
        '''
        Calculates the cylinder's area
        '''
        base_area = super().area
        lateral_area = 2 * math.pi * self.radius * self.height
        return 2 * base_area + lateral_area

    @property
    def volume(self):
        '''
        Calculates the cylinder's volume
        '''
        base_area = super().area
        return base_area * self.height
