"""
pirate.py

The Pirate class represents a pirate with a name and a weapon. It provides methods to attack enemies
and update the boat's life based on received damage.
"""
class Pirate():
    '''
    A pirate entity with attributes for name and weapon.
    Provides methods for attacking and receiving damage.
    '''

    boat_life = 200

    def __init__(self, name:str, weapon):
        '''
        Initializes a Pirate object with a name and a weapon.

        Args:
            name (str): The pirate's name.
            weapon: The pirate's weapon.
        '''
        self.name = name
        self.weapon = weapon

    def attack(self, objective_enemy):
        '''
        Performs an attack on the specified enemy.

        Args:
            objective_enemy: The enemy to be attacked.
        '''
        attack_state = True

        if self.weapon.scope == 'long':
            objective_enemy.health -= self.weapon.damage
        elif self.weapon.scope == 'short' and objective_enemy.position == 'near':
            objective_enemy.health -= self.weapon.damage
        else:
            attack_state = False

        return print(f'{self.name} attacks {objective_enemy.name}\n{"Success!" if attack_state else "Fail"}')

    @classmethod
    def hit(cls, received_damage):
        '''
        Updates the boat's life by subtracting the received damage.

        Args:
            received_damage (int): The amount of damage received.
        '''
        cls.boat_life -= received_damage
