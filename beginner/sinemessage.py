from shutil import get_terminal_size
from sys import exit
from time import sleep
from math import sin

class SineMessage:
    def __init__(s, message):
        assert 1 <= len(message) <= (s.WIDTH // 2), \
                'Message must be 1 to {} characters long.'.format(
                    s.WIDTH // 2
                )
        s.message = message