'''
constants:
    BLANK
features:
    game_board
    blank_x, blank_y
    level
methods:
    display_intro
    get_new_board
    make_move
    get_player_move
    make_random_move
    get_new_puzzle
    check_victory
    solve_automatically
    display_board
    main
'''
from random import choice

class SlidingTilePuzzle:
    BLANK = '  '
    def __init__(s, level):
        assert 3 <= int(level) <= 10, 'There must be between 3 and 10 levels'
        s.level = level
        s.blank_x = None
        s.blank_y = None
        s.game_board = [[None] * s.level] * s.level

    def display_intro():
        print('Sliding Tile Puzzle')
        print()
        print('Use the WASD keys to move the tiles')
        print('back into their original order:')
        print('      1  2  3  4')
        print('      5  6  7  8')
        print('      8 10 11 12')
        print('     13 14 15 ')
        print()    
    
    def get_new_board(s):
        s.game_board = []

        for y in range(s.level):
            for x in range(s.level):
                s.game_board[y][x] = x + y + 1
        
        s.game_board[s.level - 1][s.level - 1] = s.BLANK
        s.blank_x = s.level - 1
        s.blank_y = s.level - 1
    
    def make_move(s, move):
        if move == 'W':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y + 1][s.blank_x] = \
                s.game_board[s.blank_y + 1][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y + 1, s.blank_x
        elif move == 'A':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x + 1] = \
                s.game_board[s.blank_y][s.blank_x + 1], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y, s.blank_x + 1
        elif move == 'D':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x - 1] = \
                s.game_board[s.blank_y][s.blank_x - 1], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y, s.blank_x - 1
        elif move == 'S':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y - 1][s.blank_x] = \
                s.game_board[s.blank_y - 1][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y - 1, s.blank_x

    def get_player_move(self):
        w = 'W' if self.blank_y != self.level - 1 else ' '
        a = 'A' if self.blank_x != self.level - 1 else ' '
        s = 'S' if self.blank_y != 0 else ' '
        d = 'D' if self.blank_x != 0 else ' '

        print('                           ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))
        while True:
            response = input('> ').upper()
            if response == 'QUIT':
                exit('Thanks for playing!')
            elif response in (w+a+s+d).replace(' ', ''):
                return response
            print('Invalid move.')
            print('Enter one of {}'.format(
                (w+a+s+d).replace(' ', '')
            ))
    
    def make_random_move(s):
        valid_moves = []
        if s.blank_x != s.level - 1:
            valid_moves.append('A')
        elif s.blank_x != 0:
            valid_moves.append('D')
        elif s.blank_y != s.level - 1:
            valid_moves.append('W')
        elif s.blank_y != 0:
            valid_moves.append('S')
        
        s.make_move(choice(valid_moves))
    
    def get_new_puzzle(s, moves=200):
        s.get_new_board()
        for _ in range(moves):
            s.make_random_move()
    
    def check_victory(s):
        for y in range(s.level):
            for x in range(s.level):
                if y == s.level - 1 and x == s.level - 2:
                    return True
                if x + y != s.game_board[y][x]:
                    return False
        return True
    
    def solve_automatically(s):
        saved_state = s.game_board
        while True:
            for _ in range(40):
                s.make_random_move()
                if s.check_victory():
                    break
            if s.check_victory():
                break
            else:
                s.game_board = saved_state
        
        s.display_board()
        exit('Game over!')
    
    def display_board(s):
        labels = []
        board_string = ''
        for y in range(s.level):
            line1 = ''
            line2 = ''
            line3 = ''
            line4 = ''
            for x in range(s.level):
                labels.append(str(s.game_board[y][x]).rjust(2))
                line1 += '+------'
                line2 += '|      '
                line3 += '|  {}  '
                line4 += '|      '
            line1 += '+'
            line2 += '|'
            line3 += '|'
            line4 += '|'
            board_string += line1 + '\n'
            board_string += line2 + '\n'
            board_string += line3 + '\n'
        for x in range(s.level):
            board_string += '+------'
        board_string += '+'

        print(board_string.format(*labels))
    
    def game(s):
        while True:
            s.display_board()
            move = s.get_player_move()
            s.make_move(move)

            if s.check_victory():
                print('You won!')
                exit('Thanks for playing!')

def get_level():
    print('Please Enter game level: (3 - 10)')
    while True:
        response = input('> ')
        if response.isdecimal() and 3 <= int(response) <= 10:
                return int(response)
        print('Enter a number between 3 and 10.')

def main():
    SlidingTilePuzzle.display_intro()
    input('Press Enter to continue...')
    level = get_level()
    try:
        game = SlidingTilePuzzle(level)
        game.game()
    except KeyboardInterrupt:
        exit('Thanks for playing')

