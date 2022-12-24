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
    display_wall_dict
    paste_wall_dict
    make_wall_dict
    main
    get_player_move
    check_exit
    get_maze_from_file
    make_move

Non-class function:
    wall_str_to_wall_dict
'''

from sys import exit
from copy import copy

def wall_str_to_wall_dict(wall_str):
    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, char in enumerate(line.strip()):
            if x > width:
                width = x
            wall_dict[(x, y)] = char

    wall_dict['height'] = height
    wall_dict['width'] = width
    return wall_dict

class MazeRunner3D:
    WALL = '#'
    START = 'S'
    EXIT = 'E'
    EMPTY = ' '

    BLOCK = chr(9617)
    NORTH = 'NORTH'
    SOUTH = 'SOUTH'
    EAST = 'EAST'
    WEST = 'WEST'

    EXIT_DICT = {
        (0, 0): 'E',
        (1, 0): 'X',
        (2, 0): 'I',
        (3, 0): 'T',
        'height': 1,
        'width': 4
    }

    ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................
    '''.strip())

    CLOSED = {}

    CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____
'''.strip())

    CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.
'''.strip())

    CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________
'''.strip())

    CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.
'''.strip())

    CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..
'''.strip())

    CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..
'''.strip())
    def __init__(self):
        pass