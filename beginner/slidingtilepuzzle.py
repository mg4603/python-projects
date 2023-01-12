'''
constants:
    BLANK
features:
    game_board
    player_move
    blank_x, blank_y
    level
methods:
    display_intro
    get_new_board
    solve_automatically
    get_player_move
    get_new_puzzle
    make_move
    main
'''

class SlidingTilePuzzle:
    BLANK = '  '
    def __init__(s, level):
        assert 3 <= int(level) <= 10, 'There must be between 3 and 10 levels'
        s.level = level
        s.player_move = None
        s.blank_x = None
        s.blank_y = None
        s.game_board = [[None] * s.level] * s.level

    def display_intro():
        print('Sliding Tile Puzzle')
        print()
        print('Use the WASD keys to move the tiles')
        print('back into their original order:')
        print('      1  2  3  4')
        print('      5  6  7  8')
        print('      8 10 11 12')
        print('     13 14 15 ')
        print()    
    
    def get_new_board(s):
        s.game_board = []

        for y in range(s.level):
            for x in range(s.level):
                s.game_board[y][x] = x + y + 1
        
        s.game_board[s.level - 1][s.level - 1] = s.BLANK
        s.blank_x = s.level - 1
        s.blank_y = s.level - 1
    
    def make_move(s):
        if s.player_move == 'W':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y + 1][s.blank_x] = \
                s.game_board[s.blank_y + 1][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y + 1, s.blank_x
        elif s.player_move == 'A':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x + 1] = \
                s.game_board[s.blank_y][s.blank_x + 1], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y, s.blank_x + 1
        elif s.player_move == 'D':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x - 1] = \
                s.game_board[s.blank_y][s.blank_x - 1], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y, s.blank_x - 1
        elif s.player_move == 'S':
            s.game_board[s.blank_y][s.blank_x], \
                s.game_board[s.blank_y - 1][s.blank_x] = \
                s.game_board[s.blank_y - 1][s.blank_x], \
                s.game_board[s.blank_y][s.blank_x]
            s.blank_y, s.blank_x = s.blank_y - 1, s.blank_x
