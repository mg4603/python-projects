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

BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

class Flooder:
    HEART = chr(9829)
    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    BALL = chr(9679)
    TRIANGLE = chr(9650)
    BLOCK = chr(9608)
    LEFT_RIGHT = chr(9472)
    UP_DOWN = chr(9474)
    DOWN_RIGHT = chr(9484)
    DOWN_LEFT = chr(9488)
    UP_RIGHT = chr(9492)
    
    def __init__(self):
        pass