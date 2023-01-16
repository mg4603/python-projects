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
        return (
            (s.board['1'] == s.board['2'] == s.board['3']\
                 == s.current_player) or
            (s.board['4'] == s.board['5'] == s.board['6']\
                 == s.current_player) or
            (s.board['7'] == s.board['8'] == s.board['9']\
                 == s.current_player) or
            (s.board['1'] == s.board['4'] == s.board['7']\
                 == s.current_player) or
            (s.board['2'] == s.board['5'] == s.board['8']\
                 == s.current_player) or
            (s.board['3'] == s.board['6'] == s.board['9']\
                 == s.current_player) or
            (s.board['7'] == s.board['5'] == s.board['3']\
                 == s.current_player) or
            (s.board['1'] == s.board['5'] == s.board['9']\
                 == s.current_player)
        )

    def is_full(s):
        for space in s.ALL_SPACES:
            if s.board[space] == s.BLANK:
                return False
        return True

    def display(s):
        board_chars = []
        for space in s.ALL_SPACES:
            board_chars.append(s.board[space])
            
        print('''
        {} | {} | {}
        --+---+--
        {} | {} | {}
        --+---+--
        {} | {} | {}
'''.format(*board_chars))

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