from sys import exit
from time import sleep
try:
    from bext import goto, size
except:
    print('This program requires the bext module, which')
    print('you can install by following the instructions')
    print('at https://pypi.org/project/bext')
    exit()

class BouncingDvd:
    def __init__(self):
        self.WIDTH, self.HEIGHT = size()
        self.NUMBER_OF_LOGOS = 5
        self.PAUSE_AMOUNT = 0.2
        self.COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

        self.UP_RIGHT = 'ur'
        self.UP_LEFT = 'ul'
        self.DOWN_RIGHT = 'dr'
        self.DOWN_LEFT = 'dl'
        self.DIRECTIONS = (self.UP_RIGHT, self.UP_LEFT, self.DOWN_LEFT, self.DOWN_RIGHT)

        self.COLOR = 'color'
        self.X = 'x'
        self.Y = 'y'

    def display_intro(self):
        print('-----------------------------Bouncing DVD----------------------------')
        print('A bouncing DVD logo animation. You have to be "of a certain age" to ')
        print('appreciate this. Press Ctrl-C to stop.')
        print('NOTE: Do not resize the terminal window while this program is')
        print('running.')
        print('---------------------------------------------------------------------')
        print()

    def animate(self):
        pass

def main():
    bouncingDvd = BouncingDvd()
    bouncingDvd.animate()

if __name__ == '__main__':
    main()