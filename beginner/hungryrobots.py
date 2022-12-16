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
    add_robots
    move_robots
    get_player_move
    display_intro
'''
from random import randint
from sys import exit

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
        self.board = {'teleports': self.NUM_TELEPORTS}
        self.robots = []
        self.player_position = None
        self.player_move = None
    
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
    
    def get_new_board(self):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.board[(x, y)] = self.EMPTY_SPACE

        for x in range(self.WIDTH):
            self.board[(x, 0)] = self.WALL
            self.board[(x, self.HEIGHT - 1)] = self.WALL
        
        for y in range(self.HEIGHT):
            self.board[(0, y)] = self.WALL
            self.board[(self.WIDTH - 1, y)] = self.WALL
        
        for _ in range(self.NUM_WALLS):
            x, y = self.get_random_empty_space()
            self.board[(x, y)] = self.WALL
        
        for _ in range(self.DEAD_ROBOT):
            x, y = self.get_random_empty_space()
            self.board[(x, y)] = self.DEAD_ROBOT
    
    def add_robots(self):
        for _ in range(self.NUM_ROBOTS):
            random_x, random_y = self.get_random_empty_space()
            self.robots.append((random_x, random_y))
    
    def move_robots(self):
        player_x, player_y = self.player_position
        new_robots_positions = []

        while len(self.robots) > 0:
            robot_x, robot_y = self.robots[0]

            if robot_x < player_x:
                move_x = 1
            elif robot_x > player_x:
                move_x = -1
            elif robot_x == player_x:
                move_x = 0

            if robot_y < player_y:
                move_y = 1
            elif robot_y > player_y:
                move_y = -1
            elif robot_y == player_y:
                move_y = 0
            
            if self.board(robot_x + move_x, robot_y + move_y) == self.WALL:
                if self.board[(robot_x + move_x, robot_y)] != self.WALL:
                    move_y = 0
                elif self.board[(robot_x, robot_y + move_y)] != self.WALL:
                    move_x = 0
                else:
                    move_x = 0
                    move_y = 0

            new_robot_x = robot_x + move_x
            new_robot_y = robot_y + move_y
            
            if (
                self.board[(robot_x, robot_y)] == self.DEAD_ROBOT or
                self.board[(new_robot_x, new_robot_y)] == self.DEAD_ROBOT
            ):
                del self.robots[0]
                continue
            
            if (new_robot_x, new_robot_y) in new_robots_positions:
                new_robots_positions.remove((new_robot_x, new_robot_y))
            else:
                new_robots_positions.append((new_robot_x, new_robot_y))

            del self.robots[0]
        
        self.robots = new_robots_positions

    def main(self):
        input('Press Enter to begin...')

        self.get_new_board()
        self.add_robots()
        self.player_position = self.get_random_empty_space()

        while True:
            self.display_board()

            if len(self.robots) == 0:
                print('All the robots have crashed into each other and you')
                print('lived to tell the tale! Good Job!')
                exit()

            self.get_player_move()
            self.move_robots()

            for (x, y) in self.robots:
                if (x, y) == self.player_position:
                    self.display_board()
                    print('You have been caught by a robot!')
                    exit()
    
    def get_player_move(self):
        player_x, player_y = self.player_position
        q = 'Q' if self.is_empty(player_x - 1, player_y - 1) else ''
        w = 'W' if self.is_empty(player_x, player_y - 1) else ''
        e = 'E' if self.is_empty(player_x + 1, player_y - 1) else ''
        a = 'A' if self.is_empty(player_x - 1, player_y) else ''
        d = 'D' if self.is_empty(player_x + 1, player_y) else ''
        z = 'Z' if self.is_empty(player_x - 1, player_y + 1) else ''
        x = 'X' if self.is_empty(player_x, player_y + 1) else ''
        c = 'C' if self.is_empty(player_x + 1, player_y + 1) else ''
        all_moves = set(q, w, e, a, d, z, x, c, 'S')
        
        while True:
            print('(T)eleports remaining: {}'.format(self.board['teleports']))
            print('                     ({}) ({}) ({})'.format(q, w, e))
            print('                     ({}) (S) ({})'.format(a, d))
            print('Enter move or QUIT:  ({}) ({}) ({})'.format(z, x, c))

            move = input('> ').upper()
            if move == 'QUIT':
                exit('Thanks for playing!')
            elif move == 'T':
                self.board['teleports'] -= 1
                self.player_move = self.get_random_empty_space()
                return
            elif move != '' and move in all_moves:
                self.player_move = {
                    'Q': (player_x - 1, player_y - 1),
                    'W': (player_x, player_y - 1),
                    'E': (player_x + 1, player_y - 1),
                    'A': (player_x - 1, player_y),
                    'S': (player_x, player_y),
                    'D': (player_x + 1, player_y),
                    'Z': (player_x - 1, player_y + 1),
                    'X': (player_x, player_y + 1),
                    'C': (player_x + 1, player_y + 1),
                }[move]
                return
            else:
                print('Invalid choice. Try again.')

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('----------------------- Hungry Robots -----------------------')
        print('-------------------------------------------------------------')
        print()
        print('You are trapped in a maze with hungry robots! You don\'t know')
        print('why  robots need  to eat,  but  you don\'t want to find  out.')
        print('The robots are badly programmed and will move directly toward')
        print('you, even if blocked by walls. You must trick the robots into')
        print('crashing into  each  other (or  dead  robots)  without  begin')
        print('caught. You have a personal  teleporter device,  but it  only')
        print(
            '{} {} {}'.format(
                'has enough battery for',
                self.NUM_TELEPORTS,
                'trips. Keep in mind, you  and robots'
            )
        )
        print('can slip through the corners of two diagonal walls!')
        print()