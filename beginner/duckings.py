from time import sleep
from shutil import get_terminal_size

class DucklingsAnimation:
    def __init__(self):
        self.DUCKLING_WIDTH = 5
        self.TERMINAL_WIDTH = get_terminal_size()[0]
        self.DENSITY = 0.10

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