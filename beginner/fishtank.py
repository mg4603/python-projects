from sys import exit
from random import choice
from time import sleep

try:
    from bext import clear
except ImportError:
    print('This program requires the bext module.')
    print(
        'Find installation instructions at https://pypi.org/project/Bext/'
    )
    exit()

class FishTank:
    def __init__(self):
        pass