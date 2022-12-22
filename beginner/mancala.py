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
    def __init__(self):
        self.board = {}
        self.player_turn = None
        self.player_move = None