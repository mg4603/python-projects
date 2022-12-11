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
            player_move = self.get_player_move()
            self.change_tile(player_move, 0, 0)
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
        pass
    
    def get_player_move(self):
        pass

    def change_tile(self):
        pass

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