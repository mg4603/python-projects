from sys import exit
from random import choice
from time import sleep

try:
    from bext import clear, size
except ImportError:
    print('This program requires the bext module.')
    print(
        'Find installation instructions at https://pypi.org/project/Bext/'
    )
    exit()

class FishTank:
    WIDTH, HEIGHT = size()
    NUM_KELP = 2
    NUM_FISH = 10
    def __init__(self):
        pass