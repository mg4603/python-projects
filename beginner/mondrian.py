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
    
    def setup(s):
        s.canvas = {}
        s.number_of_segments_to_delete = 0
        s.number_of_segments_to_paint = 0
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
    
    def generate_horizontal_lines(s):
        y = randint(s.MIN_Y_INCREASE, s.MAX_Y_INCREASE)
        while 0 < y < s.height - s.MIN_Y_INCREASE:
            s.number_of_segments_to_delete += 1
            for x in range(s.width):
                s.canvas[(x, y)] = s.BLACK
            y += randint(s.MIN_Y_INCREASE, s.MAX_Y_INCREASE)
    
    def draw_canvas(s):
        for y in range(s.height):
            for x in range(s.width):
                bg(s.canvas[(x, y)])
                print(' ', end='')
            print()

    def delete_segments(s):
        for i in range(s.number_of_segments_to_delete):
            while True:
                start_x = randint(1, s.width - 2)
                start_y = randint(1, s.height - 2)
                if s.canvas[(start_x, start_y)] == s.WHITE:
                    continue

                if s.canvas[(start_x, start_y - 1)] == s.WHITE\
                        and s.canvas[(start_x, start_y + 1)] == s.WHITE:
                    orientation = 'horizontal'
                elif s.canvas[(start_x - 1, start_y)] == s.WHITE\
                        and s.canvas[(start_x + 1, start_y)] == s.WHITE:
                    orientation = 'vertical'
                else:
                    continue

                points_to_delete = set([(start_x, start_y)])
                can_delete_segment = True

                if orientation == 'vertical':
                    for change_y in (-1, 1):
                        y = start_y
                        while 0 < y < s.height - 1:
                            y += change_y
                            if (s.canvas[(start_x - 1, y)] == s.BLACK\
                                    and s.canvas[(start_x + 1, y)] == s.BLACK):
                                break
                            elif (s.canvas[(start_x - 1, y)] == s.BLACK and\
                                    s.canvas[(start_x + 1, y)] == s.WHITE) or\
                                    (s.canvas[(start_x - 1, y)] == s.WHITE and\
                                    s.canvas[(start_x + 1, y)] == s.BLACK):
                                can_delete_segment = False
                                break
                            else:
                                points_to_delete.add((start_x, y))

                elif orientation == 'horizontal':
                    for change_x in (-1, 1):
                        x = start_x
                        while 0 < x < s.width - 1:
                            x += change_x
                            if (s.canvas[(x, start_y - 1)] == s.BLACK\
                                    and s.canvas[(x, start_y + 1)] == s.BLACK):
                                break
                            elif (s.canvas[(x, start_y - 1)] == s.BLACK and \
                                    s.canvas[(x, start_y + 1)] == s.WHITE) or\
                                    (s.canvas[(x, start_y - 1 )] == s.WHITE and\
                                    s.canvas[(x, start_y + 1)] == s.BLACK):
                                can_delete_segment = False
                                break
                            else:
                                points_to_delete.add((x, start_y))
                if not can_delete_segment:
                    continue
                break

            for x, y in points_to_delete:
                s.canvas[(x, y)] = s.WHITE

    def color_canvas(s):
        for i in range(s.number_of_segments_to_paint):
            while True:
                start_x = randint(1, s.width - 2)
                start_y = randint(1, s.height - 2)

                if s.canvas[(start_x, start_y)] != s.WHITE:
                    continue
                else:
                    break
            color_to_paint = choice([s.RED, s.BLUE, s.YELLOW, s.BLACK])
            points_to_paint = set([(start_x, start_y)])
            while len(points_to_paint) > 0:
                x, y = points_to_paint.pop()
                s.canvas[(x, y)] = color_to_paint
                if s.canvas[(x - 1, y)] == s.WHITE:
                    points_to_paint.add((x - 1, y))
                if s.canvas[(x + 1, y)] == s.WHITE:
                    points_to_paint.add((x + 1, y))
                if s.canvas[(x, y + 1)] == s.WHITE:
                    points_to_paint.add((x, y + 1))
                if s.canvas[(x, y - 1)] == s.WHITE:
                    points_to_paint.add((x, y - 1))

    def main(s):
        s.setup()
        s.generate_horizontal_lines()
        s.generate_vertical_lines()

        s.number_of_segments_to_paint = s.number_of_segments_to_delete - 3
        s.number_of_segments_to_delete = int(s.number_of_segments_to_delete * 1.5)

        s.delete_segments()
        s.create_borders()

        s.color_canvas()
        s.draw_canvas()
                

if __name__ == '__main__':
    generator = MondrainGen()
    try:
        while True:
            generator.main()
            input('Press Enter to generate a new image or CTRL-C to quit.')
    except KeyboardInterrupt:
        exit()
        