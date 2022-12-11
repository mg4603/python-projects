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
    def __init__(self):
        pass