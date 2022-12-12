from sys import exit
from random import choice
try:
    from bext import clear, fg, bg
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions for the bext module')
    print('can be found at https://pypi.org/project/Bext')
    exit()

class ForestFireSim:
    TREE = 'A'
    def __init__(self):
        pass