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
from sys import exit

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
        self.winner = None
    
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

    def ask_for_player_move(self):
        while True:
            if self.player_turn == '1':
                print('Player 1, choose move: A-F (or QUIT)')
            elif self.player_turn == '2':
                print('Player2, choose move: G-L (or QUIT)')
            response = input('> ').upper().strip()

            if response == 'QUIT':
                print('Thanks for playing!')
                exit()

            if (self.player_turn == '1' and 
                response not in self.PLAYER_1_PITS) or (
                self.player_turn == '2' and 
                response not in self.PLAYER_2_PITS       
            ):
                print('Please pick a letter on your side of the board.')
                continue
            if self.board.get(response) == 0:
                print('Please pick a non-empty pit.')
                continue
            self.player_move = response

    def make_move(self):
        pit = self.player_move
        seeds_to_sow = self.board[pit]
        self.board[pit] = 0

        while seeds_to_sow > 0:
            pit = self.NEXT_PIT[pit]
            if (self.player_turn == '1' and pit == '2') or (
                self.player_turn == '2' and pit == '1'
            ):
                continue
            self.board[pit] += 1
            seeds_to_sow -= 1

        if (pit == self.player_turn == '1') or (
            pit == self.player_turn == '2'
        ):
            return
        
        if self.player_turn == '1' and pit in self.PLAYER_1_PITS \
                and self.board[pit] == 1:
            opposite_pit = self.OPPOSITE_PIT[pit]
            self.board['1'] = self.board[opposite_pit]
            self.board[opposite_pit] = 0
        elif self.player_turn == '2' and pit in self.PLAYER_2_PITS \
                and self.board[pit] == 1:
            opposite_pit = self.OPPOSITE_PIT[pit]
            self.board['2'] = self.board[opposite_pit]
            self.board[opposite_pit] = 0
        
        if self.player_turn == '2':
            self.player_turn = '1'
        elif self.player_turn == '1':
            self.player_turn = '2'

    def check_for_winner(self):
        player_1_total = (
            self.board['A'] + self.board['B'] + self.board['C'] + 
            self.board['D'] + self.board['E'] + self.board['F']
        )
        player_2_total = (
            self.board['G'] + self.board['H'] + self.board['I'] + 
            self.board['J'] + self.board['K'] + self.board['L']
        )

        if player_1_total == 0:
            self.board['2'] += player_2_total
            for pit in self.PLAYER_2_PITS:
                self.board[pit] = 0
        elif player_2_total == 0:
            self.board['1'] += player_1_total
            for pit in self.PLAYER_1_PITS:
                self.board[pit] = 0
        else:
            return 'no winner'

        if self.board['1'] > self.board['2']:
            self.winner = '1'
        elif self.board['2'] > self.board['1']:
            self.winner = '2'
        else:
            self.winner = 'tie'