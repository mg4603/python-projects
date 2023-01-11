from shutil import get_terminal_size
from sys import exit
from time import sleep
from math import sin

class SineMessage:
    WIDTH, HEIGHT = get_terminal_size()
    STEP_INC = 0.25 
    PAUSE = 0.1
    def __init__(s, message):
        s.step = 0.0
        assert 1 <= len(message) <= (s.WIDTH // 2), \
                'Message must be 1 to {} characters long.'.format(
                    s.WIDTH // 2
                )
        s.message = message
        s.multiplier = (s.WIDTH - len(s.message)) // 2
    
    def display_intro():
        print('Sine Message')
        print('Press CTRL-C to quit.')
        print()
    
    def animate(s):
        multiplier = (s.WIDTH - len(s.message)) / 2
        while True:
            padding = ' ' * int((sin(s.step) + 1) * multiplier)
            print(padding + s.message)
            sleep(s.PAUSE)
            s.step += s.STEP_INC

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

