'''
const:
    X_PLAYER
    O_PLAYER
    EMPTY

    X_HOME
    X_GOAL
    X_TRACK

    O_HOME
    O_GOAL
    O_TRACK

    ALL_SPACES
    
    FLOWER_SPACES
    BOARD_TEMPLATE

attrib:
    game_board
    player_turn
methods:
    display_board
    get_new_board
    get_player_move
    get_valid_moves
    game
    display_intro
    main()
'''

class RoyalGameOfUr:
    X_PLAYER = 'X'
    O_PLAYER = 'O'
    EMPTY = ' '
    BOARD_TEMPLATE = '''
                   {}           {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *|  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal 
                   {}           {}
'''
 
    def __init__(s):
        s.game_board = {}
        s.player_turn = s.O_PLAYER
    
    def display_intro(s):
        print('The Royal Game of Ur')
        print()
        print('This is a 5,000 year old game. Two players must move their tokens')
        print('from their home to their goal. On your turn you flip four coins')
        print('and can move one token a number of spaces equal to the heads you')
        print('got.')
        print()
        print('Ur is a racing game; the first player to move all seven of their')
        print('tokens to their goal wins. To do this, tokens must travel from')
        print('their home to their goal:')
        print()
        print('''
                X Home      X Goal
                V           ^
    +---+---+---+-v-+       +-^-+---+
    |v<<<<<<<<<<<<< |       | ^<<<< |
    |v  |   |   |   |       |   | ^ |
    +V--+---+---+---+---+---+---+-^-+
    |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
    |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
    +^--+---+---+---+---+---+---+-v-+
    |^  |   |   |   |       |   | v |
    |^<<<<<<<<<<<<< |       | V<<<< |
    +---+---+---+-^-+       +-v-+---+
                ^           v
                O Home      O Goal
    ''')
        print('If you land on an opponent\'s token in the middle track, it ')
        print('gets sent back home. The **flower** spaces let you take')
        print('another turn. Tokens in the middle flower space are safe and')
        print('cannot be landed on')

    def get_new_board(s):
        s.game_board = {s.X_HOME: 7, s.X_GOAL: 0, s.O_HOME: 7, s.O_GOAL: 0}
        for space_label in s.ALL_SPACES:
            s.game_board[space_label] = s.EMPTY
        