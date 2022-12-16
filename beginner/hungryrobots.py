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
from random import randint

class HungryRobots:
    WALL = chr(9617)
    ROBOT = 'R'
    DEAD_ROBOT = 'X'
    PLAYER = '@'
    EMPTY_SPACE = ' '

    WIDTH = 40
    HEIGHT = 20

    NUM_WALLS = 40
    NUM_TELEPORTS = 2
    NUM_DEAD_ROBOTS = 10
    NUM_ROBOTS = 10

    def __init__(self):
        self.board = {}
        self.robots = []
        self.player_position = None
    
    def is_empty(self, x, y):
        return self.board[(x, y)] == self.EMPTY_SPACE and \
            (x, y) not in self.robots
    
    def display_board(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.board[(x, y)] == self.WALL:
                    print(self.WALL, end='')
                elif self.board[(x, y)] == self.DEAD_ROBOT:
                    print(self.DEAD_ROBOT, end='')
                elif (x, y) == self.player_position:
                    print(self.PLAYER, end='')
                elif (x, y) in self.robots:
                    print(self.ROBOT, end='')
                else:
                    print(self.EMPTY_SPACE, end='')

            print()
    
    def get_random_empty_space(self):
        while True:
            random_x = randint(1, self.WIDTH - 2)
            random_y = randint(1, self.HEIGHT - 2)
            if self.is_empty(random_x, random_y):
                return (random_x, random_y)