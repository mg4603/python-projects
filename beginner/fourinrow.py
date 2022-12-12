class FourInRow:
    EMPTY_SPACE = '.'
    PLAYER_X = 'X'
    PLAYER_Y = 'O'
    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6
    COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
    def __init__(self):
        assert len(self.COLUMN_LABELS) == self.BOARD_WIDTH
        self.board = {}
        self.player_turn = self.PLAYER_X
        self.current_move = ''

    def display_intro():
        print('-------------------------------------------------------------')
        print('----------------------- Four In A Row -----------------------')
        print()
        print('Two players take turns dropping tiles into one of the seven')
        print('columns, trying to make four in a row horizontally, vertically')
        print('or diagonally.')
    
    def create_new_board(self):
        for x in range(self.BOARD_WIDTH):
            for y in range(self.BOARD_HEIGHT):
                self.board[(x, y)] = self.EMPTY_SPACE

    def get_player_move(self):
        pass

    def is_full(self):
        for x in range(self.BOARD_WIDTH):
            for y in range(self.BOARD_HEIGHT):
                if self.board[(x, y)] == self.EMPTY_SPACE:
                    return False
        
        return True

    def has_won(self):
        pass

    def display_board(self):
        tiles = []
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                tiles.append(self.board[(x, y)])

        print('''
         1234567
        +-------+
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        +-------+
        '''.format(*tiles))

    def main(self):
        pass
