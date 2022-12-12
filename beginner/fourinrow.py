class FourInRow:
    EMPTY_SPACE = '.'
    PLAYER_X = 'X'
    PLAYER_Y = 'O'
    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6
    COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
    def __init__(self):
        pass

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('----------------------- Four In A Row -----------------------')
        print()
        print('Two players take turns dropping tiles into one of the seven')
        print('columns, trying to make four in a row horizontally, vertically')
        print('or diagonally.')
