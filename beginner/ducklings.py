from time import sleep
from shutil import get_terminal_size
from random import random, choice
from sys import stdout, exit

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
    CLOSED = 'closed'
    OUT = 'out'
    DOWN = 'down'
    UP = 'up'
    HEAD = 'head'
    BODY = 'body'
    FEET = 'feet'

    def __init__(self):
        self.direction = choice([self.LEFT, self.RIGHT])
        self.body = choice([self.CHUBBY, self.VERY_CHUBBY])
        self.mouth = choice([self.OPEN, self.CLOSED])
        self.wing = choice([self.UP, self.DOWN, self.OUT])

        if self.body == self.CHUBBY:
            self.eyes = self.BEADY
        else:
            self.eyes = choice([self.BEADY, self.WIDE, self.HAPPY, self.ALOOF])

        self.part_to_display_next = self.HEAD

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
        duckling_lanes = [None] * \
            (self.TERMINAL_WIDTH // self.DUCKLING_WIDTH)

        try:
            while True:
                for lane_num, duckling_obj in enumerate(duckling_lanes):
                    if (duckling_obj == None and random() <= self.DENSITY):
                        duckling_obj = Duckling()
                        duckling_lanes[lane_num] = duckling_obj
                    
                    if duckling_obj != None:
                        print(duckling_obj.get_next_body_part(), end='')
                        if duckling_obj.part_to_display_next == None:
                            duckling_lanes[lane_num] = None
                    else:
                        print(' ' * self.DUCKLING_WIDTH, end='')                    
                print()
                stdout.flush()
                sleep(self.PAUSE)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    animator = DucklingsAnimation()
    animator.display_intro()
    animator.animate()