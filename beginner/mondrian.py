from sys import exit
from random import randint, choice

try:
    from bext import bg, size
except ImportError:
    exit('This program requires the bext module.')

class MondrainGen:
    MIN_X_INCREASE = 6
    MAX_X_INCREASE = 16

    MIN_Y_INCREASE = 3
    MAX_Y_INCREASE = 6

    WHITE = 'white'
    BLACK = 'black'
    RED = 'red'
    YELLOW = 'yellow'
    BLUE = 'blue'

    def __init__(self):
        self.width, self.height = size()
        self.canvas = {}
        self.height -= 3
        self.number_of_segments_to_delete = 0
        self.number_of_segments_to_paint = 0
    
    def setup_canvas(s):
        for y in range(s.height):
            for x in range(s.width):
                s.canvas[(x, y)] = s.WHITE
    
    def create_borders(s):
        for y in range(s.height):
            s.canvas[(0, y)] = s.BLACK
            s.canvas[(s.width - 1, y)] = s.BLACK
        
        for x in range(s.width):
            s.canvas[(x, 0)] = s.BLACK
            s.canvas[(x, s.height - 1)] = s.BLACK
    
    def generate_vertical_lines(s):
        x = randint(s.MIN_X_INCREASE, s.MAX_X_INCREASE)
        while 0 < x < s.width - s.MIN_X_INCREASE:
            s.number_of_segments_to_delete += 1
            for y in range(s.height):
                s.canvas[(x, y)] = s.BLACK
            x += randint(s.MIN_X_INCREASE, s.MAX_X_INCREASE)
        

if __name__ == '__main__':
    generator = MondrainGen()
    try:
        generator.main()
        print('Press Enter to generate a new image or CTRL-C to quit.')
    except KeyboardInterrupt:
        exit()
        