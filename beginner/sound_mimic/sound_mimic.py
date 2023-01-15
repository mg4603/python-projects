from random import choice
from time import sleep
from sys import exit

try:
    from playsound import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program.')
    print('use: python3 -m pip install playsound')
    exit()


class SoundMimic:
    PAUSE = 1
    def __init__(s):
        pass