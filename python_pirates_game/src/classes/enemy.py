'''
enemy.py
Module for handling enemy entities in a game.
Provides the Enemy class for creating and managing enemy objects.
'''

import random
from src.classes.pirate import Pirate

class Enemy():
    '''
    An enemy entity with attributes for name, health, position,
    minimum damage, and maximum damage. Provides methods for attacking and moving.
    '''
    def __init__(self, name:str, health:int, position:str, min_damage:int, max_damage:int):
        '''
        Initializes an instance of the Enemy class.

        Args:
            name (str): The name of the enemy.
            health (int): The health points of the enemy.
            position (str): The position of the enemy ('near' or 'far').
            min_damage (int): The minimum damage the enemy can inflict.
            max_damage (int): The maximum damage the enemy can inflict.

        Raises:
            ValueError: If the position is not 'near' or 'far'.
        '''
        self.name = name
        self.health = health
        self.position = position.lower()
        self.min_damage = min_damage
        self.max_damage = max_damage

        if position.lower() not in ['near', 'far']:
            raise ValueError('The value of position must be "near" or "far".')

    def attack(self, pirate):
        '''
        Attacks a pirate.

        Args:
            pirate (pirate): The pirate to be attacked.

        Returns:
            str: The message indicating the attack.
        '''
        damage = random.randint(self.min_damage, self.max_damage)
        Pirate.hit(damage)
        return print(f"Oh, no! {self.name} has attacked to {pirate.name}\nBoat's health = {0 if pirate.boat_life < 0 else pirate.boat_life}")

    def move(self):
        '''
        Moves the enemy to a different position randomly.
        '''
        if random.randint(0 , 1) == 1:
            print(f'{self.name} Moved!')
            if self.position == 'near':
                self.position = 'far'
            elif self.position == 'far':
                self.position = 'near'
