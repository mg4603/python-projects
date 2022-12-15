'''
constants:
    PAUSE_LENGTH:       time for which to pause between loop iteration
    WALL:               wall unicode
    SAND:               sand unicode
    X:                  key for tuple x value
    Y:                  key for tuple y value
    SCREEN_WIDTH:       screen width
    SCREEN_HEIGHT:      screen height
    WIDE_FALL_CHANCE:   Chance that sand falls wide(by two places instead of the normal 1)
    HOURGLASS:          set of co-ordinates that represent the hour glass
    INITIAL_SAND:       set of co-ordinates that represent the initial sand
attributes:
functions:
    display_intro
    main                main fn
    simulate:           changes values
    draw_hourglass:     draw the hourglass
'''

from random import choice
from sys import exit
from time import sleep

try:
    from bext import fg
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions can be found at')
    print('https://pypi.org/project/Bext')
    exit()

class HourGlass:
    PAUSE_LENGTH = 0.2
    WIDE_FALL_CHANCE = 50
    X = 0
    Y = 1



    def __init__(self):
        pass