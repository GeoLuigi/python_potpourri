'''
weapon.py
This module defines the Weapon class.
'''
class Weapon():
    '''
    Represents a weapon.
    '''
    def __init__(self, name:str, damage:int, scope:str):
        '''
        Initializes a Weapon object.

        Args:
            name (str): The weapon's name.
            damage (int): The weapon's damage.
            scope (str): The weapon's scope ("short" or "long").

        Raises:
            ValueError: If the scope is invalid.
        '''
        self.name = name
        self.damage = damage
        self.scope = scope.lower()

        if scope.lower() not in ['short', 'long']:
            raise ValueError('The value of scope must be "short" or "long".')
