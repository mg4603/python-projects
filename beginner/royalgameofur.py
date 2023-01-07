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