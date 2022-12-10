from shutil import get_terminal_size
from sys import exit
from pathlib import Path
from time import sleep

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
        sleep(2)
        print('\n' * 100)

    def get_canvas_string(self, file_writer):
        canvas_str = ''
        for row_num in range(self.CANVAS_HEIGHT):
            for col_num in range(self.CANVAS_WIDTH):
                if col_num == self.cursor_x and \
                        row_num == self.cursor_y \
                        and not file_writer:
                    canvas_str += '#'
                    continue
                    
                cell = self.canvas.get((col_num, row_num))
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
                elif cell == None:
                    canvas_str += ' '
            canvas_str += '\n'
        return canvas_str              

    def main(self):
        while True:
            print(self.get_canvas_string(False))
            print('WASD keys to move, H for help, C to clear,'
                +' F to save, or QUIT')
            response = input('> ').strip().upper()

            if response == 'QUIT':
                print('Thanks for playing')
                exit()
            elif response == 'H':
                print('Enter W, A, S, and D characters to move the cursor')
                print('and draw a line behind it as it moves. For example,')
                print('DDD draws a line going right and SSSDDDWWWAAA draws')
                print('a box.')
                print()
                print('You can save your drawing to a text file by entering')
                print('F and clear the canvas by pressing C')
                input('Press Enter to return to the program...')
                continue
            elif response == 'C':
                self.canvas = {}
                self.moves.append('C')
            elif response == 'F':
                print('Enter filename to save to: ')
                filename = input('> ').strip().replace(' ', '')
                if not filename.endswith('.txt'):
                    filename += '.txt'
                try:
                    with Path(filename).open('w', encoding='utf-8') as file:
                        file.write(''.join(self.moves) + '\n')
                        file.write(self.get_canvas_string(True))
                except:
                    print('Error: Could not save file.')
            
            for command in response:
                if command not in ('W', 'A', 'S', 'D'):
                    continue
                self.moves.append(command)

                if not self.canvas:
                    if command in ('W', 'S'):
                        self.canvas[(self.cursor_x, self.cursor_y)] = \
                            set(['W', 'S'])
                    elif command in ('A', 'D'):
                        self.canvas[(self.cursor_x, self.cursor_y)] = \
                             set(['A', 'D'])
                
                if command == 'W' and self.cursor_y > 0:
                    self.canvas[(self.cursor_x, self.cursor_y)].add(command)
                    self.cursor_y -= 1
                elif command == 'S' and \
                        self.cursor_y < self.CANVAS_HEIGHT - 1:
                    self.canvas[(self.cursor_x, self.cursor_y)].add(command)
                    self.cursor_y += 1
                elif command == 'A' and self.cursor_x > 0:
                    self.canvas[(self.cursor_x, self.cursor_y)].add(command)
                    self.cursor_x -= 1
                elif command == 'D' and \
                        self.cursor_x < self.CANVAS_WIDTH - 1:
                    self.canvas[(self.cursor_x, self.cursor_y)].add(command)
                    self.cursor_x += 1
                else:
                    continue

                if (self.cursor_x, self.cursor_y) not in self.canvas:
                    self.canvas[(self.cursor_x, self.cursor_y)] = set()
                
                if command == 'W':
                    self.canvas[(self.cursor_x, self.cursor_y)].add('S')
                elif command == 'S':
                    self.canvas[(self.cursor_x, self.cursor_y)].add('W')
                elif command == 'A':
                    self.canvas[(self.cursor_x, self.cursor_y)].add('D')
                elif command == 'D':
                    self.canvas[(self.cursor_x, self.cursor_y)].add('A')

if __name__ == '__main__':
    drawer = EtchingDrawer()
    drawer.display_intro()
    drawer.main()