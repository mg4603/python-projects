from time import sleep
from sys import exit
from random import randint

class DeepCave:
    def __init__(self):
        self.WIDTH = 70
        self.PAUSE_AMOUNT = 0.05

    def display_intro(self):
        print('---------------------------------------------------------------')
        print('---------------------------Deep Cave---------------------------')
        print('---------------------------------------------------------------')
        print('Press CTRL-C to stop.')
        sleep(2)
    
    def get_l_width(self):
        pass

    def get_g_width(self):
        pass

    def animate(self):
        l_width = self.get_l_width()
        g_width = self.get_g_width()  

        while True:
            try:
                r_width = self.WIDTH - g_width - l_width
                print(
                    '{}{}{}'.format(
                        ('#' * l_width), (' ' * g_width), ('#' * r_width)
                    )
                )

                dice_roll = randint(1, 6)
                if dice_roll == 1 and l_width > 1:
                    l_width -= 1
                elif dice_roll == 2 and l_width + g_width < self.WIDTH - 1:
                    l_width += 1
                else:
                    pass

                dice_roll = randint(1, 6)
                if dice_roll == 1 and g_width > 1:
                    g_width -= 1
                elif dice_roll == 2 and l_width + g_width < self.WIDTH - 1:
                    g_width += 1
                else:
                    pass
                sleep(self.PAUSE_AMOUNT)
            except KeyboardInterrupt:
                exit()

if __name__ == '__main__':
    cave = DeepCave()
    cave.display_intro()
    cave.animate()
