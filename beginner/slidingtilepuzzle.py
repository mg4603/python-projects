'''
constants:
    BLANK
features:
    game_board
    player_move
    blank_x, blank_y
    level
methods:
    solve_automatically
    get_player_move
    get_new_board
    get_new_puzzle
    make_move
    display_intro
    main
'''

class SlidingTilePuzzle:
    def __init__(s, level):
        assert 3 <= int(level) <= 10, 'There must be between 3 and 10 levels'
        s.level = level
        s.player_move = None
        s.blank_x = None
        s.blank_y = None
        s.game_board = None

