from sys import exit
from random import randint, choice

try:
    from bext import bg, size
except ImportError:
    exit('This program requires the bext module.')

class MondrainGen:
    MIN_X_INCREASE = 6
    def __init__(self):
        self.width, self.height = size()
        self.canvas = {}
        