class FourInRow:
    EMPTY_SPACE = '.'
    PLAYER_X = 'X'
    
    def __init__(self):
        pass

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('----------------------- Four In A Row -----------------------')
        print()
        print('Two players take turns dropping tiles into one of the seven')
        print('columns, trying to make four in a row horizontally, vertically')
        print('or diagonally.')
