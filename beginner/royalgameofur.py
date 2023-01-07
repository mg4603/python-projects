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
    get_player_move
    display_intro
    get_new_board
    display_board
    get_valid_moves
    game
    main()
'''

class RoyalGameOfUr:
    X_PLAYER = 'X'
    O_PLAYER = 'O'
    EMPTY = ' '

    X_HOME = 'x_home'
    X_GOAL = 'x_goal'
    X_TRACK = 'HefghijklmnopstG'

    O_HOME = 'o_home'
    O_GOAL = 'o_goal'
    O_TRACK = 'HabcdijklmnopqrG'

    ALL_SPACES = 'hgfetsijklmnopdcbarq'

    FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

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
    
    def get_player_move(s, flip_tally, valid_moves):
        print('Select token to move {} spaces: {} quit'.format(
            flip_tally,
            ' '.join(valid_moves)
        ), end='')
        while True:
            move = input('> ').lower()
            if move == 'quit':
                exit('Thanks for playing!')
            if move in valid_moves:
                return move

            print('That is not a valid move.')
    
    def display_board(s):
        x_home_tokens = (s.X_PLAYER * s.game_board[s.X_HOME]).ljust(7, '.')
        x_goal_tokens = (s.X_PLAYER * s.game_board[s.X_GOAL]).ljust(7, '.')

        o_home_tokens = (s.O_PLAYER * s.game_board[s.O_HOME]).ljust(7, '.')
        o_goal_tokens = (s.O_PLAYER * s.game_board[s.O_GOAL]).ljust(7, '.')
        spaces = [x_home_tokens, x_goal_tokens]
        for space_label in s.ALL_SPACES:
            spaces.append(s.game_board[space_label])
        spaces.extend([o_home_tokens, o_goal_tokens])

        print('\n' * 60)
        print(s.BOARD_TEMPLATE.format(*spaces))