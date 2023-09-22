'''
vector.py
Module to create instance of vectors in 2D and 3D.
'''
import math


class Vector2D():
    '''
    2D vector class
    '''
    def __init__(self, x_coordinate, y_coordinate):

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __str__(self):
        return f'({self.x_coordinate} , {self.y_coordinate})'

    @property
    def module(self):
        '''
        Calculates the 2D vector's module
        '''
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2)

    def scalar_product(self, scalar = 1):
        '''
        Multiplies the 2D vector with a given scalar number
        '''
        self.x_coordinate *= scalar
        self.y_coordinate *= scalar

    @classmethod
    def add(cls, vector_1, vector_2):
        '''
        Calculates the vectorial addition of two given 2D vectors.
        '''
        x_add = vector_1.x_coordinate + vector_2.x_coordinate
        y_add = vector_1.y_coordinate + vector_2.y_coordinate

        return cls(x_add, y_add)

    @classmethod
    def subtract(cls, vector_1, vector_2):
        '''
        Calculates the vectorial subtraction of two given 2D vectors.
        '''
        x_subtracted = vector_1.x_coordinate - vector_2.x_coordinate
        y_subtracted = vector_1.y_coordinate - vector_2.y_coordinate

        return cls(x_subtracted, y_subtracted)

    @staticmethod
    def dot_product(vector_1, vector_2):
        '''
        Calculates the dot product of two given vectors
        '''
        x_product = vector_1.x_coordinate * vector_2.x_coordinate
        y_product = vector_1.y_coordinate * vector_2.y_coordinate

        return x_product + y_product

    @staticmethod
    def distance(vector_1, vector_2):
        '''
        Calculates the distance between two given vectors.
        '''
        return math.sqrt((vector_1.x_coordinate - vector_2.x_coordinate) ** 2 + (vector_1.y_coordinate - vector_2.y_coordinate) ** 2)

    @classmethod
    def zero(cls):
        '''
        Returns a zero 2D vector
        '''
        return cls(0, 0)

    def extend_to_3d(self, z_coordinate = 0):
        '''
        Extends a 2D vector in to a 3D vector with its z coordinate = 0 as default
        '''
        return Vector3D(self.x_coordinate, self.y_coordinate, z_coordinate)

class Vector3D(Vector2D):
    '''
    3D vector class
    '''
    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        super().__init__(x_coordinate, y_coordinate)

        self.z_coordinate = z_coordinate

    def __str__(self):
        return f'({self.x_coordinate} , {self.y_coordinate} , {self.z_coordinate})'

    @property
    def module(self):
        '''
        Calculates the 3D vector's module
        '''
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2 + self.z_coordinate ** 2)

    def scalar_product(self, scalar=1):
        '''
        Multiplies the 3D vector with a given scalar number
        '''
        super().scalar_prod(scalar)
        self.z_coordinate = scalar * self.z_coordinate

    @classmethod
    def add(cls, vector_1, vector_2):
        '''
        Calculates the vector addition of two given 3D vectors.
        '''
        x_add = vector_1.x_coordinate + vector_2.x_coordinate
        y_add = vector_1.y_coordinate + vector_2.y_coordinate
        z_add = vector_1.z_coordinate + vector_2.z_coordinate

        return cls(x_add, y_add, z_add)

    @classmethod
    def subtract(cls, vector_1, vector_2):
        '''
        Calculates the vector subtraction of two given 3D vectors.
        '''
        x_subtracted = vector_1.x_coordinate - vector_2.x_coordinate
        y_subtracted = vector_1.y_coordinate - vector_2.y_coordinate
        z_subtracted = vector_1.z_coordinate - vector_2.z_coordinate

        return cls(x_subtracted, y_subtracted, z_subtracted)

    @staticmethod
    def dot_product(vector_1, vector_2):
        '''
        Calculates the dot product between two 3D vectors given
        '''
        return super().dot_product(vector_1, vector_2) + vector_1.z_coordinate * vector_2.z_coordinate

    @staticmethod
    def distance(vector_1, vector_2):
        return math.sqrt((super().distance(vector_1, vector_2)) ** 2 + (vector_1.z_coordinate - vector_2.z_coordinate) ** 2)

    @classmethod
    def zero(cls):
        '''
        Returns a zero 3D vector
        '''
        return cls(0 , 0 , 0)

    @classmethod
    def horizontal(cls):
        '''
        Returns a horizontal 3D vector
        '''
        return cls(1, 0, 0)

    @classmethod
    def vertical(cls):
        '''
        Returns a vertical 3D vector
        '''
        return cls(0, 1, 0)

    @classmethod
    def forward(cls):
        '''
        Returns a forward 3D vector
        '''
        return cls(0, 0, 1)


