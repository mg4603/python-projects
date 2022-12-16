'''
const:
    WALL:           chr(9617)
    ROBOT:          R
    DEAD_ROBOT:     X
    PLAYER:         @
    WIDTH:
    HEIGHT
    EMPTY_SPACE     ' '
    NUM_WALLS       40
    NUM_DEAD_ROBOTS 10
    NUM_TELEPORTS   2
    NUM_ROBOTS      10
attributes:
    board = {}
    robots
    player_position
methods:
    display_board
    main
    is_empty
    get_random_empty_space
    get_new_board
    get_robots
'''

class HungryRobots:
    def __init__(self):
        self.board = {}
        self.robots = []
        self.player_position = None