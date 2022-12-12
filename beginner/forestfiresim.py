from sys import exit
from random import choice
from time import sleep
try:
    from bext import clear, fg, bg
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions for the bext module')
    print('can be found at https://pypi.org/project/Bext')
    exit()

class ForestFireSim:
    TREE = 'A'
    FIRE = 'W'
    EMPTY = ' '
    def __init__(
            self, screen_width, screen_height, 
            initial_tree_density, grow_chance,
            fire_chance, pause_length
            ):
        if is_positive_int(screen_width):
            self.screen_width = int(screen_width)
        if is_positive_int(screen_height):
            self.screen_height = int(screen_height)
        if is_positive_float(initial_tree_density):
            self.initial_tree_density = float(initial_tree_density)
        if is_positive_float(grow_chance):
            self.grow_chance = float(grow_chance)
        if is_positive_float(fire_chance):
            self.fire_chance = fire_chance
        if is_positive_float(pause_length):
            self.pause_length = pause_length

    def display_intro():
        print('-------------------------------------------------------------')
        print('---------------------- Forest Fire Sim ----------------------')
        print('-------------------------------------------------------------')
        print('A simulation of wildfires spreading in a forest.')
        print('Press CTRL-C to stop...')
        print()
        sleep(2)

    def main(self):
        pass

WIDTH = 79
HEIGHT = 22
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5