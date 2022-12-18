'''
LangtonsAnt
const:
    WIDTH:              terminal width
    HEIGHT:             terminal height

    ANT_UP
    ANT_DOWN
    ANT_LEFT
    ANT_RIGHT

    ANT_COLOR
    BLACK_TILE
    WHITE_TILE

    PAUSE_AMOUNT:       0.1
    NUMBER_OF_ANTS:     10

    NORTH:              North
    SOUTH:              south
    EAST:               east
    WEST:               west

attributes:
    board
    changed_tiles
    ants

methods:
    main
    display_intro
    display_board
'''

try:
    from bext import fg, bg, clear, goto
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions can be found at')
    print('https://pypi.org/project/Bext')

from sys import exit
from random import choice, randint
from time import sleep

class LangtonsAnt:
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

    PAUSE_AMOUNT = 0.1
    NUM_OF_ANTS = 10
    def __init__(self):
        pass
