from sys import exit
from random import randint, choice

try:
    from bext import bg, size
except ImportError:
    exit('This program requires the bext module.')

class MondrainGen:
    MIN_X_INCREASE = 6
    MAX_X_INCREASE = 16

    MIN_Y_INCREASE = 3
    MAX_Y_INCREASE = 6

    WHITE = 'white'
    def __init__(self):
        self.width, self.height = size()
        self.canvas = {}
        