from time import sleep
from sys import exit
from random import randint

class DeepCave:
    def __init__(self):
        self.WIDTH = 70
        self.PAUSE_AMOUNT = 0.05
        self.l_width = 0
        self.g_width = 0

    def display_intro(self):
        print('---------------------------------------------------------------')
        print('---------------------------Deep Cave---------------------------')
        print('---------------------------------------------------------------')
        print('Press CTRL-C to stop.')
        sleep(2)
    
    def get_l_width(self):
        print('Enter left width (1-{}), or QUIT.'.format(self.WIDTH-2))
        while True:
            response = input('> ').strip()
            
            if response.upper() == 'QUIT':
                exit()
            elif not (response.isdecimal() and 1 <= int(response) <= self.WIDTH - 2):
                print('Enter an integer between 1 and {}'.format(self.WIDTH - 2))
            else:
                self.l_width = int(response)
                return


    def get_g_width(self):
        pass

    def animate(self):
        self.get_l_width()
        self.get_g_width()  

        while True:
            try:
                r_width = self.WIDTH - self.g_width - self.l_width
                print(
                    '{}{}{}'.format(
                        ('#' * self.l_width), (' ' * self.g_width), ('#' * r_width)
                    )
                )

                dice_roll = randint(1, 6)
                if dice_roll == 1 and self.l_width > 1:
                    self.l_width -= 1
                elif dice_roll == 2 and self.l_width + self.g_width < self.WIDTH - 1:
                    self.l_width += 1
                else:
                    pass

                dice_roll = randint(1, 6)
                if dice_roll == 1 and self.g_width > 1:
                    self.g_width -= 1
                elif dice_roll == 2 and self.l_width + self.g_width < self.WIDTH - 1:
                    self.g_width += 1
                else:
                    pass
                sleep(self.PAUSE_AMOUNT)
            except KeyboardInterrupt:
                exit()

if __name__ == '__main__':
    cave = DeepCave()
    cave.display_intro()
    cave.animate()
