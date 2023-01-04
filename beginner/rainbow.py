from time import sleep
from sys import exit
try:
    from bext import fg
except ImportError:
    exit('This program requires the bext module.')

class Rainbow:
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    INDIGO = 'cyan'
    VIOLET = 'purple'
    def __init__(s):
        pass