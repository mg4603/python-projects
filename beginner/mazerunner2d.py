'''
const:
    WALL:               representation of wall in maze file
    EMPTY:              representation of empty in maze file
    START:              representation of start in maze file
    EXIT:               representation of exit in maze file
    PLAYER:             display symbol of player
    BLOCK:              display symbol of wall
attributes:
    height
    width
    maze
    player_x
    player_y
    exit_x
    exit_y
methods:
    display_maze
    get_player_move
    move_player
    check_winner
    main
'''

class MazeRunner2D:
    WALL = '#'
    EMPTY = ' '
    START = 'S'
    EXIT = 'E'

    PLAYER = '@'
    BLOCK = chr(9617)

    def __init__(self):
        self.height = 0
        self.width = 0
        self.maze = {}
        self.player_x = None
        self.player_y = None
        self.exit_x = None
        self.exit_y = None