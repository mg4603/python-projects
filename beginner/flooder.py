try:
    from bext import bg, fg, clear
except ImportError:
    print('Import Error: This program needs the bext module to run.')
    print(
        '{} \n{}'.format(
            'Installation instructions can be found at', 
            'https://pypi.org/project/bext'
        )
    )
    exit()

from random import choice, randint
from sys import exit

BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

class Flooder:
    HEART = chr(9829)
    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    BALL = chr(9679)
    TRIANGLE = chr(9650)
    BLOCK = chr(9608)
    LEFT_RIGHT = chr(9472)
    UP_DOWN = chr(9474)
    DOWN_RIGHT = chr(9484)
    DOWN_LEFT = chr(9488)
    UP_RIGHT = chr(9492)
    UP_LEFT = chr(9496)

    TILE_TYPES = (0, 1, 2, 3, 4, 5)
    COLORS_MAP = {
        0: 'red',
        1: 'green',
        2: 'blue',
        3: 'yellow',
        4: 'cyan',
        5: 'purple'
    }
    COLOR_MODE = 'color mode'
    SHAPES_MAP = {
        0: HEART,
        1: TRIANGLE,
        2: DIAMOND,
        3: BALL,
        4: CLUB,
        5: SPADE
    }
    SHAPE_MODE = 'shape mode'
    
    def __init__(self, board_width, board_height, moves_per_game):
        if is_positive_int(board_width):
            self.board_width = int(board_width)
        if is_positive_int(board_height):
            self.board_height = int(board_height)
        if is_positive_int(moves_per_game):
            self.moves_left = moves_per_game
        
        self.game_board = {}
        self.get_new_board()
        self.display_mode = ''
        self.current_move = ''
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('-------------------------- Flooder --------------------------')
        print('-------------------------------------------------------------')
        print('Set the upper left color/ shape, which fills in all the')
        print('adjacent squares of that color shape. Try to make the entire')
        print('board the same color/ shape.')
    
    def main(self):
        bg('black')
        fg('white')
        clear()
        print('Do you want to play in color blind mode? (Y/N)')
        response = input('> ').upper()
        if response.startswith('Y'):
            self.display_mode = self.SHAPE_MODE
        else:
            self.display_mode = self.COLOR_MODE
        
        while True:
            self.display_board()

            print('Moves Left: {}'.format(self.moves_left))
            self.get_player_move()
            self.change_tile(0, 0)
            self.moves_left -= 1

            if self.has_won():
                self.display_board()
                print('You have won!')
                break
            elif self.moves_left == 0:
                self.display_board()
                print('You have run out of moves!')
                break
    
    def get_new_board(self):
        for x in range(self.board_width):
            for y in range(self.board_height):
                self.game_board[(x, y)] = choice(self.TILE_TYPES)
        
        for i in range(self.board_width * self.board_height):
            x = randint(0, self.board_width - 2)
            y = randint(0, self.board_height - 1)
            self.game_board[(x + 1, y)] = self.game_board[(x, y)]

    def display_board(self):
        fg('white')
        print('{}{}{}'.format(
            self.DOWN_RIGHT,
            (self.LEFT_RIGHT * self.board_width),
            self.DOWN_LEFT
        ))

        for y in range(self.board_height):
            fg('white')
            if y == 0:
                print('>', end='')
            else:
                print(self.UP_DOWN, end='')
            
            for x in range(self.board_width):
                fg(self.COLORS_MAP[self.game_board[(x, y)]])
                if self.display_mode == self.COLOR_MODE:
                    print(self.BLOCK, end='')
                elif self.display_mode == self.SHAPE_MODE:
                    print(self.SHAPE_MODE[self.game_board[(x, y)]], end='')
            
            fg('white')
            print(self.UP_DOWN)

        print('{}{}{}'.format(
            self.UP_RIGHT, 
            (self.LEFT_RIGHT * self.board_width),
            self.UP_LEFT
        ))
    
    def get_player_move(self):
        while True:
            fg('white')
            print('Choose one of ', end='')

            if self.display_mode == self.COLOR_MODE:
                fg('red')
                print('(R)ed ', end='')
                fg('green')
                print('(G)reen ', end='')
                fg('blue')
                print('(B)lue ', end='')
                fg('yellow')
                print('(Y)ellow ', end='')
                fg('cyan')
                print('(C)yan ', end='')
                fg('purple')
                print('(P)urple ', end='')
            elif self.display_mode == self.COLOR_MODE:
                fg('red')
                print('(H)eart ', end='')
                fg('green')
                print('(T)riangle ', end='')
                fg('blue')
                print('(D)iamond ', end='')
                fg('yellow')
                print('(B)all ', end='')
                fg('cyan')
                print('(C)lub ', end='')
                fg('purple')
                print('(S)pade ', end='')
            fg('white')
            print('or QUIT:')
            response = input('> ').upper()
            if response == 'QUIT':
                print('Thanks for playing!')
                exit()
            if self.display_mode == self.COLOR_MODE and\
                    response in tuple('RGBYCP'):
                self.current_move = {
                    'R': 0,
                    'G': 1,
                    'B': 2,
                    'Y': 3,
                    'C': 4,
                    'P': 5
                }[response]
                return
            elif self.display_mode == self.SHAPE_MODE and\
                    response in tuple('HTDBCS'):
                self.current_move = {
                    'H': 0,
                    'T': 1,
                    'D': 2,
                    'B': 3,
                    'C': 4,
                    'S': 5
                }[response]
                return

    def change_tile(self, x, y, char_to_change=None):
        if x == 0 and y == 0:
            char_to_change = self.game_board[(x, y)]
            if self.current_move == char_to_change:
                return

        self.game_board[(x, y)] = self.current_move

        if x > 0 and self.game_board[(x - 1), y] == char_to_change:
            self.change_tile(x - 1, y, char_to_change)
        if y > 0 and self.game_board[(x, y - 1)] == char_to_change:
            self.change_tile(x, y - 1, char_to_change)
        if x < self.board_width - 1 and self.game_board[(x + 1, y)] == char_to_change:
            self.change_tile(x + 1, y, char_to_change)
        if y < self.board_height - 1 and self.game_board[(x, y + 1)] == char_to_change:
            self.change_tile(x, y + 1, char_to_change)
        
    def has_won(self):
        pass

def is_positive_int(number):
    try:
        number = int(number)
        if not ((number > 0) and (number % 1 == 0)):
            return False
        return True
    except:
        return False 

if __name__ == '__main__':
    game = Flooder(BOARD_WIDTH, BOARD_HEIGHT, MOVES_PER_GAME)
    game.display_intro()
    game.main()