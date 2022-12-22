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
'''
from sys import exit

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
            elif move == 'A' and \
                    self.maze[(self.player_x - 1, self.player_y)] == \
                    self.EMPTY:
                self.player_move = 'A'
            elif move == 'S' and \
                    self.maze[(self.player_x, self.player_y - 1)] == \
                    self.EMPTY:
                self.player_move = 'S'
            elif move == 'D' and \
                    self.maze[(self.player_x + 1, self.player_y)] == \
                    self.EMPTY:
                self.player_move = 'D'
            
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