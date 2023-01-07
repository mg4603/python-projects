from time import sleep
from math import cos, sin
from sys import platform, exit
from os import system

class RotatingPolyhedron:
    PAUSE_AMOUNT = 0.1

    WIDTH = 80
    HEIGHT = 24

    SCALE_X = (WIDTH - 4) // 8
    SCALE_Y = (HEIGHT - 4) // 8
    SCALE_Y *= 2
    
    TRANSLATE_X = (WIDTH - 4) // 2
    TRANSLATE_Y = (HEIGHT - 4) // 2

    LINE_CHAR = '*'

    X_ROTATE_SPEED = 0.03

    def __init__(s):
        pass