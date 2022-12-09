from time import sleep
from shutil import get_terminal_size

class Duckling:
    LEFT = 'left'
    RIGHT = 'right'
    BEADY = 'beady'
    WIDE = 'wide'
    HAPPY = 'happy'
    ALOOF = 'aloof'
    CHUBBY = 'chubby'
    VERY_CHUBBY = 'very chubby'
    OPEN = 'open'

    def __init__(self):
        pass


class DucklingsAnimation:
    DUCKLING_WIDTH = 5
    TERMINAL_WIDTH = get_terminal_size()[0]
    DENSITY = 0.10
    PAUSE = 0.2
    def __init__(self):
        pass

    def display_intro(self):
        print('--------------------------------------------------------------')
        print('---------------------Duckling Screensaver---------------------')
        print('--------------------------------------------------------------')
        print('Press CTRL-C to quit...')
        print()
        sleep(2)

    def animate(self):
        pass

if __name__ == '__main__':
    animator = DucklingsAnimation()
    animator.display_intro()
    animator.animate()