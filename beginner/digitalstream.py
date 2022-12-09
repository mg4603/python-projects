from shutil import get_terminal_size
from time import sleep
from sys import exit, stdout
from random import choice, random, randint

class DigitalStream:
    def __init__(self):
        self.MIN_STREAM_LENGTH = 6
        self.MAX_STREAM_LENGTH = 14
        self.PAUSE = 0.1
        self.STREAM_CHARS = ['0', '1']

        self.DENSITY = 0.2

        self.WIDTH = get_terminal_size()[0]
    
    def display_intro(self):
        print('--------------------------------------------------------------')
        print('------------------Digital Stream Screensaver------------------')
        print('--------------------------------------------------------------')
        print('Press CTRL-C to quit.')
        print()
        sleep(2)

    def animation(self):
        try:
            columns = [0] * self.WIDTH
            while True:
                for i in range(self.WIDTH):
                    if columns[i] == 0:
                        if random() <= self.DENSITY:
                            columns[i] = randint(
                                self.MIN_STREAM_LENGTH, self.MAX_STREAM_LENGTH
                            )
                        
                    if columns[i] > 0:
                        print(choice(self.STREAM_CHARS), end='')
                        columns[i] -= 1
                    else:
                        print(' ', end='')
                print()
                stdout.flush()
                sleep(self.PAUSE)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    digital_stream = DigitalStream()
    digital_stream.display_intro()
    digital_stream.animation()