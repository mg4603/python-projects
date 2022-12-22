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
    check_completion
    generate_maze_from_file
    main
    display_intro
'''
from sys import exit
from pathlib import Path

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
        self.player_move = None
    
    def display_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == (self.player_x, self.player_y):
                    print(self.player_y, end='')
                elif (x, y) == (self.exit_x, self.exit_y):
                    print('X', end='')
                elif self.maze[(x, y)] == self.WALL:
                    print(self.BLOCK, end='')
                else:
                    print(' ', end='')
            print()
    
    def check_completion(self):
        if (self.player_x, self.player_y) == (self.exit_x, self.exit_y):
            return True
        else:
            return False
    
    def get_player_move(self):
        while True:
            print('                          W')
            print('Enter direction or QUIT: ASD')

            move = input('> ').upper()
            if move == 'QUIT':
                exit('Thanks for playing!')
            
            if move not in ['W', 'A', 'S', 'D']:
                print('Invalid direction. Enter one of W, A, S, or D.')
                continue

            if move == 'W' and \
                    self.maze[(self.player_x, self.player_y - 1)] == \
                    self.EMPTY:
                self.player_move = 'W'
                return
            elif move == 'A' and \
                    self.maze[(self.player_x - 1, self.player_y)] == \
                    self.EMPTY:
                self.player_move = 'A'
                return
            elif move == 'S' and \
                    self.maze[(self.player_x, self.player_y - 1)] == \
                    self.EMPTY:
                self.player_move = 'S'
                return
            elif move == 'D' and \
                    self.maze[(self.player_x + 1, self.player_y)] == \
                    self.EMPTY:
                self.player_move = 'D'
                return
            
            print('You cannot move in that direction.')
    
    def move_player(self):
        if self.player_move == 'W':
            while True:
                self.player_y -= 1
                if (self.player_x, self.player_y) == \
                        (self.exit_x, self.exit_y):
                    break
                elif self.maze[(self.player_x, self.player_y - 1)] \
                        == self.WALL:
                    break
                elif self.maze[(self.player_x + 1, self.player_y)] == \
                        self.EMPTY or \
                        self.maze[(self.player_x - 1, self.player_y)] == \
                        self.EMPTY:
                    break
        elif self.player_move == 'S':
            while True:
                self.player_y += 1
                if (self.player_x, self.player_y) == \
                        (self.exit_x, self.exit_y):
                    break
                elif self.maze[(self.player_x, self.player_y + 1)] \
                        == self.WALL:
                    break
                elif self.maze[(self.player_x + 1, self.player_y)] == \
                        self.EMPTY or \
                        self.maze[(self.player_x - 1, self.player_y)] == \
                        self.EMPTY:
                    break
        elif self.player_move == 'A':
            while True:
                self.player_x -= 1
                if (self.player_x, self.player_y) == \
                        (self.exit_x, self.exit_y):
                    break
                elif self.maze[(self.player_x - 1, self.player_y)] \
                        == self.WALL:
                    break
                elif self.maze[(self.player_x, self.player_y + 1)] == \
                        self.EMPTY or \
                        self.maze[(self.player_x, self.player_y - 1)] == \
                        self.EMPTY:
                    break
        elif self.player_move == 'D':
            while True:
                self.player_y += 1
                if (self.player_x, self.player_y) == \
                        (self.exit_x, self.exit_y):
                    break
                elif self.maze[(self.player_x + 1, self.player_y)] \
                        == self.WALL:
                    break
                elif self.maze[(self.player_x, self.player_y + 1)] == \
                        self.EMPTY or \
                        self.maze[(self.player_x, self.player_y - 1)] == \
                        self.EMPTY:
                    break

    def generate_maze_from_file(self):
        while True:
            print('Enter the filename of the maze (or LIST or QUIT):')
            response = input('> ')

            if response.upper() == 'QUIT':
                exit('Thanks for playing')
            elif response.upper() == 'LIST':
                cwd = Path('.')
                print('Maze files found in {}:'.format(cwd.name))
                for file in cwd.glob('*.txt'):
                    if str(file.name).startswith('maze'):
                        print('     {}'.format(str(file.name)))
                continue
            
            filename = Path(response)
            if filename.exists() and filename.is_file():
                break

            print('There is no file named {}'.format(response))
        
        with filename.open('r') as file:
            lines = file.readlines()
        
        self.width = len(lines[0].rstrip())
        y = 0
        for line in lines:
            for x, char in enumerate(line.rstrip()):
                assert char in [self.WALL, self.EMPTY, self.START, self.EXIT],\
                    'Invalid character at column {}, line {}'.format(x + 1, y + 1)
                if char in (self.WALL, self.EMPTY):
                    self.maze[(x, y)] = char
                elif char == self.START:
                    self.maze[(x, y)] = self.EMPTY
                    self.player_x, self.player_y = x, y
                elif char == self.EXIT:
                    self.maze[(x, y)] = self.EMPTY
                    self.exit_x, self.exit_y = x, y
            y += 1

        self.height = y
    
    def display_intro(self):
        print('--------------------------------------------------------------')
        print('------------------------Maze Runner 2D------------------------')
        print('--------------------------------------------------------------')

    def main(self):
        self.display_intro()
        self.generate_maze_from_file()
        assert self.player_x != None and self.player_y != None, \
            'No start in maze file'
        assert self.exit_x != None and self.exit_y != None, \
            'No exit in maze file'
        
        while True:
            self.check_completion()
            self.display_maze()

            self.get_player_move()

            self.move_player()
