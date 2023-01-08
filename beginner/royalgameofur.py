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
    
    def get_valid_moves(s, flip_tally):
        valid_moves = []
        if s.player_turn == s.X_PLAYER:
            opponent = s.O_PLAYER
            track = s.X_TRACK
            home = s.X_HOME
        elif s.player_turn == s.O_PLAYER:
            opponent = s.X_PLAYER
            track = s.O_TRACK
            home = s.O_HOME
        
        if s.game_board[home] > 0 and \
                s.game_board[track[flip_tally]] == s.EMPTY:
            valid_moves.append('home')
        
        for track_space_index, space_label in enumerate(track):
            if space_label == 'H' or space_label == 'G' or \
                    s.game_board[space_label] != s.player_turn:
                continue
            next_track_space_index = track_space_index + flip_tally
            next_track_space_key = track[next_track_space_index]
            if next_track_space_index >= len(track):
                continue
            else:
                if next_track_space_key == 'G':
                    valid_moves.append(space_label)
                    continue

            if s.game_board[next_track_space_key] in (s.EMPTY, opponent):
                if next_track_space_key == 'l' and \
                        s.game_board[next_track_space_index] == opponent:
                    continue
                valid_moves.append(space_label)
        return valid_moves
    
    def game(s):
        while True:
            if s.player_turn == s.O_PLAYER:
                track = s.O_TRACK
                goal = s.O_GOAL
                home = s.O_HOME
                opponent = s.X_PLAYER
                opponent_home = s.X_HOME
            elif s.player_turn == s.X_PLAYER:
                track = s.X_TRACK
                home = s.X_HOME
                goal = s.X_GOAL
                opponent = s.O_PLAYER
                opponent_home = s.O_HOME
            
            s.display_board()

            input('It\'s {}\'s turn. Press Enter to flip.'.format(
                s.player_turn
            ))

            flip_tally = s.get_flip_tally()

            if flip_tally == 0:
                input('You lose a turn. Press Enter to continue...')
                s.player_turn = opponent
                continue

            valid_moves = s.get_valid_moves(flip_tally)

            if valid_moves == []:
                print('There are no possible moves, so you lose a turn.')
                input('Press Enter to continue...')
                s.player_turn = opponent
                continue
            
            move = s.get_player_move(flip_tally, valid_moves)

            if move == 'home':
                s.game_board[home] -= 1
                next_space_index = flip_tally
            else:
                s.game_board[move] = s.EMPTY
                next_space_index = track.index(move) + flip_tally
            
            if track[next_space_index] == 'G':
                s.game_board[goal] += 1
                if s.game_board[goal] == 7:
                    s.display_board()
                    print('{} has won the game!'.format(s.player_turn))
                    exit('Thanks for playing!')
            else:
                if s.game_board[track[next_space_index]] == opponent:
                    s.game_board[opponent_home] += 1
                s.game_board[track[next_space_index]] = s.player_turn
            
            if track[next_space_index] in s.FLOWER_SPACES:
                print('{} landed on a flower space and goes again.')
                input('Press Enter to continue...')
            else:
                s.player_turn = opponent
