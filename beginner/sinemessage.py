from shutil import get_terminal_size
from sys import exit
from time import sleep
from math import sin

class SineMessage:
    WIDTH, HEIGHT = get_terminal_size()
    STEP = 0.0
    STEP_INC = 0.25 
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
    
def get_message():
    WIDTH, _ = get_terminal_size()
    print(
        'What message do you want to display? (MAX {} chars.)'.format(
            WIDTH // 2
        )
    )
    while True:
        message = input('> ')
        if 1 <= len(message) <= (WIDTH // 2):
            return message
        print('Message must be 1 to {} characters long.'.format(WIDTH // 2))

