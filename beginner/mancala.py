'''
const:
    PLAYER_1_PITS
    PLAYER_2_PITS
    OPPOSITE_PIT
    NEXT_PIT
    PIT_LABELS
    STARTING_NUMBER_OF_SEEDS
attribs:
    board
    player_turn
    player_move
methods:
    get_new_board
    ask_for_player_move
    make_move
    check_for_winner
    display_intro
    main
'''
class Mancala:
    PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
    PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')
    OPPOSITE_PIT = {
        'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
        'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'
    }
    NEXT_PIT = {
        'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 
        'F': '1', '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 
        'I': 'H', 'H': 'G', 'G': '2', '2': 'A'
    }
    PIT_LABELS = 'ABCDEF1LKJIHG2'
    STARTING_NUMBER_OF_SEEDS = 4
    def __init__(self):
        self.board = {}
        self.player_turn = None
        self.player_move = None
    
    def get_new_board(self):
        return {
            '1': 0,
            '2': 0,
            'A': self.STARTING_NUMBER_OF_SEEDS,
            'B': self.STARTING_NUMBER_OF_SEEDS,
            'C': self.STARTING_NUMBER_OF_SEEDS,
            'D': self.STARTING_NUMBER_OF_SEEDS,
            'E': self.STARTING_NUMBER_OF_SEEDS,
            'F': self.STARTING_NUMBER_OF_SEEDS,
            'G': self.STARTING_NUMBER_OF_SEEDS,
            'H': self.STARTING_NUMBER_OF_SEEDS,
            'I': self.STARTING_NUMBER_OF_SEEDS,
            'J': self.STARTING_NUMBER_OF_SEEDS,
            'K': self.STARTING_NUMBER_OF_SEEDS,
            'L': self.STARTING_NUMBER_OF_SEEDS
        }
    
    def display_board(self):
        seed_amount = []
        for pit in 'GHIJKL21ABCDEF':
            number_of_seeds_in_this_pit = str(self.board[pit]).rjust(2)
            seed_amount.append(number_of_seeds_in_this_pit)
        
        print('''
+------+------+------+--<<<<<-Player 2----+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T   
O      |F     |E     |D     |C     |B     |A     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+
'''.format(*seed_amount))
        