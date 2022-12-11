try:
    from bext import bg
except ImportError:
    print('Import Error: This program needs the bext module to run.')
    print(
        '{} \n{}'.format(
            'Installation instructions can be found at', 
            'https://pypi.org/project/bext'
        )
    )
    exit()

from random import choice
from sys import exit

class Flooder:
    BOARD_WIDTH = 16
    BOARD_HEIGHT = 14
    MOVES_PER_GAME = 20

    HEART = chr(9829)
    
    def __init__(self):
        pass