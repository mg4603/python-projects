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
    def __init__(self):
        pass

    def display_intro():
        print('-------------------------------------------------------------')
        print('---------------------- Forest Fire Sim ----------------------')
        print('-------------------------------------------------------------')
        print('A simulation of wildfires spreading in a forest.')
        print('Press CTRL-C to stop...')
        print()
        sleep(2)


WIDTH = 79
HEIGHT = 22
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01

PAUSE_LENGTH = 0.5