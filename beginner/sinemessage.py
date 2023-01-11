from shutil import get_terminal_size
from sys import exit
from time import sleep
from math import sin

class SineMessage:
    WIDTH, HEIGHT = get_terminal_size()
    def __init__(s, message):
        assert 1 <= len(message) <= (s.WIDTH // 2), \
                'Message must be 1 to {} characters long.'.format(
                    s.WIDTH // 2
                )
        s.message = message
    
    def display_intro():
        print('Sine Message')
        print('Press CTRL-C to quit.')
        print()