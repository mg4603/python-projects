from sys import exit
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
        

    def animate(self):
        pass

def main():
    bouncingDvd = BouncingDvd()
    bouncingDvd.animate()

if __name__ == '__main__':
    main()