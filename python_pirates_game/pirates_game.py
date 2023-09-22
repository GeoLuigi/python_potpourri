'''
Pirates Game (pirates_game)

This script simulates a battle between pirates and enemies.
It defines classes for weapons, pirates, and enemies.
The battle consists of pirates attacking enemies and enemies attacking
pirates in turns until all enemies are defeated or the pirate's boat's life reaches 0.

Author: Jorge L. Hurtado G.

Date: May - 2023
'''

import time
import random
from src.classes.enemy import Enemy
from src.classes.pirate import Pirate
from src.classes.weapon import Weapon


# Defining the weapons:
sword = Weapon('sword', 3, 'short')
ax = Weapon('ax', 5, 'short')
bow = Weapon('bow', 2, 'long')

# Defining the enemies:
torvellino_1 = Enemy('Torvellino 1', 25, 'near', 2, 5)
torvellino_2 = Enemy('Torvellino 2', 25, 'near', 4, 8)
torvellino_3 = Enemy('Torvellino 3', 25, 'far', 3, 5)
torvellino_4 = Enemy('Torvellino 4', 25, 'far', 6, 9)

enemies = [torvellino_1, torvellino_2, torvellino_3, torvellino_4]

# Defining the pirates:
pyratilla = Pirate('Pyratilla', sword)
pym = Pirate('Pym', bow)
pyerce = Pirate('Pyerce', ax)

pirates = [pyratilla, pym, pyerce]

def restart_values():
    '''
    Restarts the game values by setting all the health values
    (including the boat's life) to their default value.
    '''
    Pirate.boat_life = 200

    # Restoring enemies life:
    for index in range(0, 4):
        enemies[index].health = 25

def start_new_battle():
    '''
    Restarts the battle
    '''
    restart_values()
    battle()


def battle():
    '''
    The battle starts
    '''

    game_over = False
    # Creates a copy of the original list of enemies
    # and creates a new list with the active enemies.
    battle_enemies = enemies.copy()
    active_enemies = enemies.copy()

    print('=========================================')
    print('=========== THE BATTLE BEGINS ===========')
    print('=========================================')

    # Starts the iteration for the enemies in the original list.
    for enemy in battle_enemies:
        while enemy.health > 0:
            # Pirates attack in order to the same enemy
            print('\n' + '*' * 30)
            print("Pirates' turn:\n")
            for pirate in pirates:

                # In order to break te loop
                if enemy not in active_enemies:
                    break
                pirate.attack(enemy)
                print(f"{enemy.name}'s health = {0 if enemy.health <= 0 else enemy.health}")

                # Removing an enemy if it's health == 0
                if enemy.health <= 0:
                    print(f'xxxx {enemy.name} defeated xxxx')
                    active_enemies.remove(enemy)
            print('*' * 30)

            # the action below only works if there are still active enemies
            if len(active_enemies) > 0:
                game_over = True
                # The enemies attack in order to a random pirate
                print('\n' + '/' * 60)
                print("Enemies' turn:")
                for active_enemy in active_enemies:
                    state_decision = random.randint(0, 1)
                    attacked_pirate = random.choice(pirates)

                    # Decides if the enemy attacks or moves
                    if state_decision == 1:
                        print(f'{active_enemy.name} is deciding either to move or not...')
                        initial_enemy_state = active_enemy.position
                        active_enemy.move()
                        if initial_enemy_state == active_enemy.position:
                            print("It didn't move")
                    else:
                        active_enemy.attack(attacked_pirate)

                    # If the boat's life == 0, restarts the game
                    if attacked_pirate.boat_life <= 0:
                        print('+++++++++++ GAME OVER +++++++++++\n')
                        start_new_battle()
                print('/' * 60)

    if game_over:
        print('CONGRATS!!! All the enemies were defeated')
    time.sleep(60)
battle()
