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
    
    def get_head_str(self):
        head_str = ''
        if self.direction == self.LEFT:
            #mouth
            if self.mouth == self.OPEN:
                head_str += '>'
            elif self.mouth == self.CLOSED:
                head_str += '='

            #eyes
            if self.eyes == self.BEADY and self.body == self.CHUBBY:
                head_str += '"'
            elif self.eyes == self.BEADY and self.body == self.VERY_CHUBBY:
                head_str += '" '
            elif self.eyes == self.WIDE:
                head_str += '\' \''
            elif self.eyes == self.HAPPY:
                head_str += '^ ^'
            elif self.eyes == self.ALOOF:
                head_str += '` `'

            #back_of_head
            head_str += ')'

        if self.direction == self.RIGHT:
            #back_of_head
            head_str += '('

            #eyes
            if self.eyes == self.BEADY and self.body == self.CHUBBY:
                head_str += '"'
            elif self.eyes == self.BEADY and self.body == self.VERY_CHUBBY:
                head_str += ' "'
            elif self.eyes == self.WIDE:
                head_str += '\' \''
            elif self.eyes == self.HAPPY:
                head_str += '^ ^'
            elif self.eyes == self.ALOOF:
                head_str += '` `'

            #mouth
            if self.mouth == self.OPEN:
                head_str += '<'
            elif self.mouth == self.CLOSED:
                head_str += '='
        
        if self.body == self.CHUBBY:
            head_str += ' '
        
        return head_str

    def get_body_str(self):
        body_str = '('
        if self.direction == self.LEFT:
            # interior body space
            if self.body == self.CHUBBY:
                body_str += ' '
            elif self.body == self.VERY_CHUBBY:
                body_str += '  '

            # wings
            if self.wing == self.UP:
                body_str += '^'
            elif self.wing == self.DOWN:
                body_str += 'v'
            elif self.wing == self.OUT:
                body_str += '>'

        if self.direction == self.RIGHT:
            # wings
            if self.wing == self.UP:
                body_str += '^'
            elif self.wing == self.DOWN:
                body_str += 'v'
            elif self.wing == self.OUT:
                body_str += '<'

            # interior body space
            if self.body == self.CHUBBY:
                body_str += ' '
            elif self.body == self.VERY_CHUBBY:
                body_str += '  '

        if self.body == self.CHUBBY:
            body_str += ' '
        body_str += ')'

        return body_str


    def get_feet_str(self):
        pass

    def get_next_body_part(self):
        if self.part_to_display_next == self.HEAD:
            self.part_to_display_next = self.BODY
            return self.get_head_str()
        elif self.part_to_display_next == self.BODY:
            self.part_to_display_next = self.FEET
            return self.get_body_str()
        elif self.part_to_display_next == self.FEET:
            self.part_to_display_next = None
            return self.get_feet_str()

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