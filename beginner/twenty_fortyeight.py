from random import randint
from sys import exit

class Twenty48Board:
    def __init__(s):
        pass

    def get_new_board(s):
        pass

    def display(s):
        pass

    def _combine_columns(s):
        pass

    def make_move(s):
        pass

    def add_two_to_board(s):
        pass

    def is_full(s):
        pass

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