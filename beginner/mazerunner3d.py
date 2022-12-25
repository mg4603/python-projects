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
    get_maze_from_file
    main
    get_player_move
    check_exit
    make_move

Non-class function:
    wall_str_to_wall_dict
'''

from sys import exit
from copy import copy
from pathlib import Path

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

    PASTE_CLOSED_TO = {
        'A': (6, 4),
        'B': (4, 3),
        'C': (3, 1),
        'D': (10, 3),
        'E': (0, 0),
        'F': (12, 0)
    }

    def __init__(self):
        self.player_x = None
        self.player_y = None
        self.exit_x = None
        self.exit_y = None
        self.player_direction = self.NORTH
        self.maze = {}
        self.maze_height = 0
        self.maze_width = 0
        self.current_wall_dict = {}

    def display_wall_dict(s):
        print(s.BLOCK * (s.current_wall_dict['width'] + 2))
        for y in range(s.current_wall_dict['height']):
            print(s.BLOCK, end='')
            for x in range(s.current_wall_dict['width']):
                wall = s.current_wall_dict[(x, y)]
                if wall == '.':
                    wall = ' '
                print(wall, end='')
            print(s.BLOCK)
        print(s.BLOCK * (s.current_wall_dict['width'] + 2))

    def paste_wall_dict(s, src_wall_dict, dest_wall_dict, top, left):
        dest_wall_dict = copy(dest_wall_dict)
        for x in range(src_wall_dict['width']):
            for y in range(src_wall_dict['height']):
                dest_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
        return dest_wall_dict
    
    def make_wall_dict(s):
        if s.player_direction == s.NORTH:
            #  A
            # BCD
            # E@F
            offsets = (
                ('A',  0, -2),
                ('B', -1, -1),
                ('C',  0, -1),
                ('D',  1, -1),
                ('E', -1,  0),
                ('F',  1,  0),
            )
        elif s.player_direction == s.SOUTH:
            # F@E
            # DCB
            #  A
            offsets = (
                ('A',  0,  2),
                ('B',  1,  1),
                ('C',  0,  1),
                ('D', -1,  1),
                ('E',  1,  0),
                ('F', -1,  0)
            )
        elif s.player_direction == s.EAST:
            # EB
            # @CA
            # FD
            offsets = (
                ('A',  2,  0),
                ('B',  1, -1),
                ('C',  1,  0),
                ('D',  1,  1),
                ('E',  0, -1),
                ('F',  0,  1)
            )
        elif s.player_direction == s.WEST:
            #  DF
            # AC@
            #  BE
            offsets = (
                ('A', -2,  0),
                ('B', -1,  1),
                ('C', -1,  0),
                ('D', -1, -1),
                ('E',  0,  1),
                ('F',  0, -1)
            )

        section = {}
        for sec, off_x, off_y in offsets:
            section[sec] = s.maze.get(
                (s.player_x + off_x, s.player_y + off_y), s.WALL
            )
            if (s.player_x + off_x, s.player_y + off_y) == \
                    (s.exit_x, s.exit_y):
                section[sec] = s.EXIT
        
        s.current_wall_dict = copy(s.ALL_OPEN)

        for sec in 'ABCDEF':
            if section[sec] == s.WALL:
                s.current_wall_dict = s.paste_wall_dict(
                    s.CLOSED[sec], s.current_wall_dict, 
                    s.PASTE_CLOSED_TO[sec][0], s.PASTE_CLOSED_TO[sec][1]
                )
        
        if section['C'] == s.EXIT:
            s.current_wall_dict = s.paste_wall_dict(
                s.EXIT_DICT, s.current_wall_dict, 7, 9
            )
        if section['E'] == s.EXIT:
            s.current_wall_dict = s.paste_wall_dict(
                s.EXIT_DICT, s.current_wall_dict, 0, 11
            )
        if section['F'] == s.EXIT:
            s.current_wall_dict = s.paste_wall_dict(
                s.EXIT_DICT, s.current_wall_dict, 13, 11
            )
    
    def display_intro(s):
        print('Maze Runner 3D')
        print()
    
    def get_maze_from_file(s):
        while True:
            print('Enter the filename of the maze (or LIST or QUIT):')
            response = input('> ').strip()

            if response.upper() == 'QUIT':
                exit('Thanks for playing!')
            
            if response.upper() == 'LIST':
                cwd = Path('.')
                print('Maze files found in {}'.format(cwd.name))
                for file in cwd.glob('*.txt'):
                    if str(file).startswith('maze'):
                        print('     {}'.format(file.name))
                continue
            
            file_path = Path(response)
            if file_path.exists() and file_path.is_file():
                break
            print('There is no file named {}'.format(file_path.name))
        
        with file_path.open('r') as file:
            lines = file.readlines()
        
        s.maze_width = len(lines[0].strip())
        s.maze_height = len(lines)
        for y,line in enumerate(lines):
            for x, char in enumerate(line):
                assert char in (s.WALL, s.EMPTY, s.START, s.EXIT), \
                    'Invalid character at column {}, line {}'.format(x + 1, y + 1)
                if char in (s.WALL, s.EMPTY):
                    s.maze[(x, y)] = char
                elif char == s.START:
                    s.player_x, s.player_y = x, y
                    s.maze[(x, y)] = s.EMPTY
                elif char == s.EMPTY:
                    s.exit_x, s.exit_y = x, y
                    s.maze[(x, y)] = s.EMPTY
    
    