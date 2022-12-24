'''
const:
    WALL:       representation in mazefile
    START:      representation in mazefile
    EXIT:       representation in mazefile
    EMPTY:      representation in mazefile

    BLOCK
    NORTH
    SOUTH
    EAST
    WEST

    EXIT_DICT
    ALL_OPEN
    CLOSED
    PASTE_CLOSED_TO
    

attributes:
    maze
    player_x
    player_y
    exit_x
    exit_y
    height
    width
    player_direction

methods:
    wall_str_to_wall_dict
    display_wall_dict
    paste_wall_dict
    make_wall_dict
    main
    get_player_move
    check_exit
    get_maze_from_file
    make_move
'''

from sys import exit
from copy import copy

class MazeRunner3D:
    WALL = '#'
    START = 'S'
    EXIT = 'E'
    EMPTY = ' '

    BLOCK = chr(9617)
    NORTH = 'NORTH'
    def __init__(self):
        pass