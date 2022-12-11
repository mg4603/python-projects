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
    UP_LEFT = chr(9496)

    TILE_TYPES = (0, 1, 2, 3, 4, 5)
    COLORS_MAP = {
        0: 'red',
        1: 'green',
        2: 'blue',
        3: 'yellow',
        4: 'cyan',
        5: 'purple'
    }
    COLOR_MODE = 'color mode'
    SHAPES_MAP = {
        0: HEART,
        1: TRIANGLE,
        2: DIAMOND,
        3: BALL,
        4: CLUB,
        5: SPADE
    }
    SHAPE_MODE = 'shape mode'
    
    def __init__(self, board_width, board_height, moves_per_game):
        if is_positive_int(board_width):
            self.board_width = int(board_width)
        if is_positive_int(board_height):
            self.board_height = int(board_height)
        if is_positive_int(moves_per_game):
            self.moves_per_game = moves_per_game
        