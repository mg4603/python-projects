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
    NUM_BUBBLERS = 1
    FRAMES_PER_SECOND = 4

    FISH_TYPES = [
        {
            'right': ['><>'],
            'left': ['<><'],
        },
        {
            'right': ['>||>'],
            'left': ['<||<']
        },
        {
            'right': ['>))>'],
            'left': ['<((<']
        },
        {
            'right': ['>||o', '>||.'],
            'left': ['o||<', '.||<']
        },
        {
            'right': ['>))o', '>)).'],
            'left': ['o((<', '.((<']
        },
        {
            'right': ['>-==>'],
            'left': ['<==-<']
        },
        {
            'right': [r'>\\>'],
            'left': ['<//<']
        },
        {
            'right': ['><)))*>'],
            'left': ['<*(((><']
        },
        {
            'right': ['}-[[[*>'],
            'left': ['<*]]]-{']
        },
        {
            'right': [']-<)))b>'],
            'left': ['<d(((<-[']
        },
        {
            'right': ['><XXX*>'],
            'left': ['<*XXX><']
        },
        {
            'right': [
                '_.-._.^=>', '.-._.-.^=>',
                '-._.-._^=>', '._.-._.^=>'
            ],
            'left': [
                '<=^._.-._', '<=^.-._.-.',
                '<=^_.-._.-', '<=^._.-._.'
            ]
        }

    ]

    LONGEST_FISH_LENGTH = 10
    LEFT_EDGE = 0
    

    def __init__(self):
        pass