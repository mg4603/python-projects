from sys import exit
from random import random
from time import sleep
try:
    from bext import clear, fg, bg, goto
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions for the bext module')
    print('can be found at https://pypi.org/project/Bext')
    exit()

def is_positive_int(number):
    try:
        number = int(number)
        if not(number > 0 and number % 1 == 0):
            return False
        return True
    except:
        return False

def is_positive_float(number):
    try:
        number = float(number)
        if not(number > 0):
            return False
        return True
    except:
        return False

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
        
        self.forest = {}

    def display_intro():
        print('-------------------------------------------------------------')
        print('---------------------- Forest Fire Sim ----------------------')
        print('-------------------------------------------------------------')
        print('A simulation of wildfires spreading in a forest.')
        print('Press CTRL-C to stop...')
        print()
        sleep(2)

    def create_forest(self):
        self.forest['width'] = self.screen_width
        self.forest['height'] = self.screen_height
        for x in range(self.screen_width):
            for y in range(self.screen_height):
                if random() <= self.initial_tree_density:
                    self.forest[(x, y)] = self.TREE
                else:
                    self.forest[(x, y)] = self.EMPTY

    def display_forest(self):
        goto(0, 0)
        for y in range(self.forest['height']):
            for x in range(self.forest['width']):
                if self.forest[(x, y)] == self.TREE:
                    fg('green')
                    print(self.TREE, end = '')
                elif self.forest[(x, y)] == self.FIRE:
                    fg('red')
                    print(self.FIRE, end='')
                elif self.forest[(x, y)] == self.EMPTY:
                    print(self.EMPTY, end='')
            print()
        fg('reset')
        print('Grow change: {}%'.format(
            self.grow_chance * 100
        ), end='')
        print('Lightning change: {}%'.format(
            self.fire_chance * 100
        ), end='')
        print('Press CTRL-C to quit...')

    def main(self):
        pass

WIDTH = 79
HEIGHT = 22
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5