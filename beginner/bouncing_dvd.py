from sys import exit
from time import sleep
from random import choice, randint
from sys import stdout
try:
    from bext import goto, size, clear, fg
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
        self.COLORS = [
            'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
            ]

        self.UP_RIGHT = 'ur'
        self.UP_LEFT = 'ul'
        self.DOWN_RIGHT = 'dr'
        self.DOWN_LEFT = 'dl'
        self.DIRECTIONS = (
            self.UP_RIGHT, self.UP_LEFT, self.DOWN_LEFT, self.DOWN_RIGHT
            )

        self.COLOR = 'color'
        self.X = 'x'
        self.Y = 'y'
        self.DIR = 'direction'

    def display_intro(self):
        print('-----------------------------Bouncing DVD----------------------------')
        print('A bouncing DVD logo animation. You have to be "of a certain age" to ')
        print('appreciate this. Press Ctrl-C to stop.')
        print('NOTE: Do not resize the terminal window while this program is')
        print('running.')
        print('---------------------------------------------------------------------')
        print()

    def animate(self):
        clear()

        logos = []
        for i in range(self.NUMBER_OF_LOGOS):
            logos.append({
                self.COLOR: choice(self.COLORS),
                self.X: randint(1, self.WIDTH -4),
                self.Y: randint(1, self.HEIGHT - 4),
                self.DIR: choice(self.DIRECTIONS)
            })
            if logos[-1][self.X] % 2 == 1:
                logos[-1][self.X] -= 1
        
        corner_bounces = 0
        while True:
            for logo in logos:
                goto(logo[self.X], logo[self.Y])
                print('   ', end='')

                original_direction = logo[self.DIR]

                #bouncing off corners
                if logo[self.X] == 0 and logo[self.Y] == 0:
                    logo[self.DIR] = self.DOWN_RIGHT
                    corner_bounces += 1
                elif logo[self.X] == 0 and logo[self.Y] == self.HEIGHT - 1:
                    logo[self.DIR] = self.UP_RIGHT
                    corner_bounces += 1
                elif logo[self.X] == self.WIDTH - 3 and logo[self.Y] == 0:
                    logo[self.DIR] = self.DOWN_LEFT
                    corner_bounces += 1
                elif logo[self.X] == self.WIDTH - 3 and \
                        logo[self.Y] == self.HEIGHT - 1:
                    logo[self.DIR] = self.UP_LEFT
                    corner_bounces += 1
                #bouncing off edges
                # left edge
                elif logo[self.X] == 0 and logo[self.DIR] == self.UP_LEFT:
                    logo[self.DIR] = self.UP_RIGHT
                elif logo[self.X] == 0 and logo[self.DIR] == self.DOWN_LEFT:
                    logo[self.DIR]  = self.DOWN_RIGHT
                # right edge
                elif logo[self.X] == self.WIDTH - 3 and \
                        logo[self.DIR] == self.UP_RIGHT:
                    logo[self.DIR] = self.UP_LEFT
                elif logo[self.X]  == self.WIDTH - 3 and \
                        logo[self.DIR] == self.DOWN_RIGHT:
                    logo[self.DIR] = self.DOWN_LEFT
                # top edge
                elif logo[self.Y] == 0 and logo[self.DIR] == self.UP_RIGHT:
                    logo[self.DIR] = self.DOWN_RIGHT
                elif logo[self.Y] == 0  and logo[self.DIR] == self.UP_LEFT:
                    logo[self.DIR] = self.DOWN_LEFT
                # bottom edge
                elif logo[self.Y] == self.HEIGHT - 1 and \
                        logo[self.DIR] == self.DOWN_LEFT:
                    logo[self.DIR] = self.UP_LEFT
                elif logo[self.Y] == self.HEIGHT - 1 and \
                        logo[self.DIR] == self.DOWN_RIGHT:
                    logo[self.DIR]  = self.UP_RIGHT
                
                if logo[self.DIR] != original_direction:
                    logo[self.COLOR] = choice(self.COLORS)
                
                # Move the logo
                # X moves by 2 because terminal chars are twice as tall as they 
                # are wide
                if logo[self.DIR] == self.UP_LEFT:
                    logo[self.Y] -= 1
                    logo[self.X] -= 2
                if logo[self.DIR] == self.UP_RIGHT:
                    logo[self.Y] -= 1
                    logo[self.X] += 2
                if logo[self.DIR] == self.DOWN_LEFT:
                    logo[self.Y] += 1
                    logo[self.X] -= 2
                if logo[self.DIR] == self.DOWN_RIGHT:
                    logo[self.Y] += 1
                    logo[self.X] += 2
            
            # display number of corner bounces
            goto(5, 0)
            fg('white')
            print(f'Corner bounces: {corner_bounces}', end='')

            for logo in logos:
                goto(logo[self.X], logo[self.Y])
                fg(logo[self.COLOR])
                print('DVD', end='')
            
            goto(0, 0)
            
            stdout.flush()
            sleep(self.PAUSE_AMOUNT)

def main():
    bouncingDvd = BouncingDvd()
    bouncingDvd.display_intro()
    sleep(10)
    try:
        bouncingDvd.animate()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo')
        exit()


if __name__ == '__main__':
    main()