from shutil import get_terminal_size
from sys import exit
from pathlib import Path

class EtchingDrawer:
    UP_DOWN_CHAR = chr(9474)
    LEFT_RIGHT_CHAR = chr(9472)
    DOWN_RIGHT_CHAR = chr(9484)
    DOWN_LEFT_CHAR = chr(9488)
    UP_RIGHT_CHAR = chr(9492)
    UP_LEFT_CHAR = chr(9496)
    UP_DOWN_RIGHT_CHAR = chr(9500)
    UP_DOWN_LEFT_CHAR = chr(9508)
    DOWN_LEFT_RIGHT_CHAR = chr(9516)
    UP_LEFT_RIGHT_CHAR = chr(9624)
    CROSS_CHAR = chr(9532)
    
    def __init__(self):
        self.CANVAS_WIDTH, self.CANVAS_HEIGHT = get_terminal_size()
        self.CANVAS_HEIGHT -= 5
        self.canvas = {}
        self.cursor_x = 0
        self.cursor_y = 0
        self.moves = []

    def display_intro(self):
        print('--------------------------------------------------------------')
        print('------------------------Etching Drawer------------------------')
        print('--------------------------------------------------------------')
        print('An art program that draws a continuous line around the screen')
        print('using the WASD keys. Inspired by Etch A Sketch toys.')
        print('')
        print('For example you can draw Hilbert Curve fractal with:')
        print('SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW')
        print('')

    def get_canvas_string(self, file_writer):
        canvas_str = ''
        for row_num in range(self.CANVAS_HEIGHT):
            for col_num in range(self.CANVAS_WIDTH):
                if row_num == self.cursor_x and \
                        col_num == self.cursor_y \
                        and not file_writer:
                    canvas_str += '#'
                    continue
                    
                cell = self.canvas.get((row_num, col_num))
                if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                    canvas_str += self.UP_DOWN_CHAR
                elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                    canvas_str += self.LEFT_RIGHT_CHAR
                elif cell == set(['S', 'D']):
                    canvas_str += self.DOWN_RIGHT_CHAR
                elif cell == set(['S', 'A']):
                    canvas_str += self.DOWN_LEFT_CHAR
                elif cell == set(['W', 'D']):
                    canvas_str += self.UP_RIGHT_CHAR
                elif cell == set(['W', 'A']):
                    canvas_str += self.UP_LEFT_CHAR
                elif cell == set(['W', 'S', 'D']):
                    canvas_str += self.UP_DOWN_RIGHT_CHAR
                elif cell == set(['W', 'S', 'A']):
                    canvas_str += self.UP_DOWN_LEFT_CHAR
                elif cell == set(['A', 'S', 'D']):
                    canvas_str += self.DOWN_LEFT_RIGHT_CHAR
                elif cell == set(['W', 'A', 'D']):
                    canvas_str += self.UP_LEFT_RIGHT_CHAR
                elif cell == set(['W', 'A', 'S', 'D']):
                    canvas_str += self.CROSS_CHAR
            canvas_str += '\n'
        return canvas_str              

    def main(self):
        pass