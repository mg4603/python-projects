from sys import exit

class TicTacToeBoard:
    ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    BLANK = ' '
    X = 'X'
    O = 'O'
    def __init__(s):
        s.board = s.get_blank_board()
        s.current_player = s.X
        s.next_player = s.O
    
    def has_line(s):
        pass

    def is_full(s):
        pass

    def display(s):
        pass

    def get_blank_board(s):
        board = {}
        for space in s.ALL_SPACES:
            board[space] = s.BLANK
        return board

    def make_move(s):
        pass

def main():
    print('Welcome to Tic-TacToe!')
    board = TicTacToeBoard()
    while True:
        board.display()

        print('What is {}\'s move? (1-9 or QUIT)')
        move = input('> ').upper()

        if move == 'QUIT':
            exit('Thanks for playing!')
        
        if board.make_move(): # if move can be made
            pass
        else:
            pass

        if board.has_line():
            print('{} has won!'.format(board.current_player))
            exit('Thanks for playing!')
        elif board.is_full():
            print('It\'s a tie!')
            exit('Thanks for playing!')

if __name__ == '__main__':
    main()