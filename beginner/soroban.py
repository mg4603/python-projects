class Soroban:
    NUM_OF_DIGITS = 10

    def __init__(s):
        s.board = s.create_board()

    def create_board(s):
        seg_sep = f'+{"=" * 3 * s.NUM_OF_DIGITS}==+\n'
        board = seg_sep
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' 
        board += f'I {" | " * s.NUM_OF_DIGITS} I\n' 
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' 
        board += seg_sep
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' * 6
        board += f'+{"=={}" * s.NUM_OF_DIGITS}==+'
        return board
    
    def display_controls(s):
        print('  +q w e r t y u i o p')
        print('  -a s d f g h j k l ;')
        print('(Enter a number, "quit", or a stream of up/down letters.)')

    def display_board(s):
        pass
