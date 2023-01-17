from random import randint
from sys import exit
from copy import copy

class Twenty48Board:
    BLANK = ' '
    def __init__(s):
        s.board = {}
        s.get_new_board()

    def get_new_board(s):
        for y in range(4):
            for x in range(4):
                s.board[(x, y)] = s.BLANK
        
        starting_twos_placed = 0
        while starting_twos_placed < 2:
            random_space = randint(0, 3), randint(0, 3)
            if s.board[random_space] == s.BLANK:
                s.board[random_space] = 2
                starting_twos_placed += 1

    def display(s):
        labels = []
        for y in range(4):
            for x in range(4):
                label = str(s.board[(x, y)]).center(5)
                labels.append(label)
        
        print('''
        +-----+-----+-----+-----+
        |     |     |     |     |
        |{}|{}|{}|{}|
        |     |     |     |     |
        +-----+-----+-----+-----+
        |     |     |     |     |
        |{}|{}|{}|{}|
        |     |     |     |     |
        +-----+-----+-----+-----+
        |     |     |     |     |
        |{}|{}|{}|{}|
        |     |     |     |     |
        +-----+-----+-----+-----+
        |     |     |     |     |
        |{}|{}|{}|{}|
        |     |     |     |     |
        +-----+-----+-----+-----+

        '''.format(*labels))


    def _combine_columns(s):
        pass

    def make_move(s, move):
        if move not in ('W', 'A', 'S', 'D'):
            return
        
        if move == 'W':
            all_column_spaces = [
                [(0, 0), (0, 1), (0, 2), (0, 3)],
                [(1, 0), (1, 1), (1, 2), (1, 3)],
                [(2, 0), (2, 1), (2, 2), (2, 3)],
                [(3, 0), (3, 1), (3, 2), (3, 3)],
            ]
        elif move == 'A':
            all_column_spaces = [
                [(0, 0), (1, 0), (2, 0), (3, 0)],
                [(0, 1), (1, 1), (2, 1), (3, 1)],
                [(0, 2), (1, 2), (2, 2), (3, 2)],
                [(0, 3), (1, 3), (2, 3), (3, 3)],
            ]
        elif move == 'D':
            all_column_spaces = [
                [(3, 0), (2, 0), (1, 0), (0, 0)],
                [(3, 1), (2, 1), (1, 1), (0, 1)],
                [(3, 2), (2, 2), (1, 2), (0, 2)],
                [(3, 3), (2, 3), (1, 3), (0, 3)],
            ]
        elif move == 'S':
            all_column_spaces = [
                [(0, 3), (0, 2), (0, 1), (0, 0)],
                [(1, 3), (1, 2), (1, 1), (1, 0)],
                [(2, 3), (2, 2), (2, 1), (2, 0)],
                [(3, 3), (3, 2), (3, 1), (3, 0)],
            ]
        
        new_board = {}
        for column_space in all_column_spaces:
            column = []
            for space in column_space:
                column.append(s.board[space])
            
            combined_tiles_column = s._combine_columns(column)

            i = 0
            for space in column_space:
                new_board[space] = combined_tiles_column[i]
                i += 1
        
        s.board = copy(new_board)

    def add_two_to_board(s):
        while True:
            random_space = randint(0, 3), randint(0, 3)
            if s.board[random_space] == s.BLANK:
                s.board[random_space] = 2
                return

    def is_full(s):
        for y in range(4):
            for x in range(4):
                if s.board[(x, y)] == s.BLANK:
                    return False
        return True
    
    def get_score(s):
        score = 0
        for y in range(4):
            for x in range(4):
                if s.board[(x, y)] != s.BLANK:
                    score += s.board[(x, y)]
        return score

def display_intro():
    print('Twenty Forty-eight')
    print()
    print('Slide all the tiles on the board in one of the four directions.')
    print('Tiles with like numbers will combine into large-numbered tiles.')
    print('A new 2 tile is added to the board on each move. You win if you')
    print('can create a 2048 tile. You lose if tiles fill up the board')
    print('before then.')
    print()

def get_player_move():
    print('Enter move: (WASD or Q to quit)')
    while True:
        move = input('> ').strip().upper()

        if move == 'Q':
            exit('Thanks for playing!')

        if move in ('W', 'A', 'S', 'D'):
            return move
        
        print('Enter one of "W", "A", "S", "D", or "Q".')

def main():
    board = Twenty48Board()
    display_intro()
    input('Press Enter to begin...')
    while True:
        print('Score: {}'.format(board.get_score()))
        board.display()
        
        move = get_player_move()
        board.make_move(move)

        board.add_two_to_board()

        if board.is_full():
            board.display()
            exit('Game over - Thanks for playing!')

if __name__ == '__main__':
    main()