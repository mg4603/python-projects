'''
LangtonsAnt
const:
    WIDTH:              terminal width
    HEIGHT:             terminal height

    ANT_UP
    ANT_DOWN
    ANT_LEFT
    ANT_RIGHT

    ANT_COLOR
    BLACK_TILE
    WHITE_TILE

    PAUSE_AMOUNT:       0.1
    NUMBER_OF_ANTS:     10

    NORTH:              North
    SOUTH:              south
    EAST:               east
    WEST:               west

attributes:
    board
    changed_tiles
    ants

methods:
    main
    display_intro
    display_board
'''

try:
    from bext import fg, bg, clear, goto, size
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions can be found at')
    print('https://pypi.org/project/Bext')

from sys import exit, stdout
from random import choice, randint
from time import sleep
from copy import copy

class LangtonsAnt:
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

    PAUSE_AMOUNT = 0.1
    NUM_OF_ANTS = 10

    ANT_COLOR = 'red'
    BLACK_TILE = 'black'
    WHITE_TILE = 'white'

    ANT_UP = '^'
    ANT_DOWN = 'v'
    ANT_LEFT = '>'
    ANT_RIGHT = '<'

    WIDTH, HEIGHT = size()
    def __init__(self):
        self.HEIGHT -= 1
        self.board = {'width': self.WIDTH, 'height': self.HEIGHT}
        self.changed_tiles = []
        self.ants = []
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('----------------------- Langton\'s Ant -----------------------')
        print('-------------------------------------------------------------')
        print()
        sleep(2)
    
    def setup_simulation(self):
        fg(self.ANT_COLOR)
        bg(self.WHITE_TILE)
        clear()
        for _ in range(self.NUM_OF_ANTS):
            ant = {
                'x': randint(0, self.WIDTH - 1),
                'y': randint(0, self.HEIGHT - 1),
                'direction': choice((self.NORTH, self.SOUTH, self.EAST, self.WEST))
            }
            self.ants.append(ant)
    
    def main(self):
        self.setup_simulation()
        while True:
            self.display_board()
            self.changed_tiles = []
            next_board = copy(self.board)

            for ant in self.ants:
                if self.board.get((ant['x'], ant['y']), False) == True:
                    next_board[(ant['x'], ant['y'])] = False
                    if ant['direction'] == self.NORTH:
                        ant['direction'] = self.EAST
                    elif ant['direction'] == self.EAST:
                        ant['direction'] = self.SOUTH
                    elif ant['direction'] == self.SOUTH:
                        ant['direction'] = self.WEST
                    elif ant['direction'] == self.WEST:
                        ant['direction'] = self.NORTH
                else:
                    next_board[(ant['x'], ant['y'])] = True
                    if ant['direction'] == self.NORTH:
                        ant['direction'] = self.WEST
                    elif ant['direction'] == self.WEST:
                        ant['direction'] = self.SOUTH
                    elif ant['direction'] == self.SOUTH:
                        ant['direction'] = self.EAST
                    elif ant['direction'] == self.EAST:
                        ant['direction'] = self.NORTH
                self.changed_tiles.append((ant['x'], ant['y']))

                if ant['direction'] == self.NORTH:
                    ant['y'] -= 1
                elif ant['direction'] == self.SOUTH:
                    ant['y'] += 1
                elif ant['direction'] == self.EAST:
                    ant['x'] += 1
                elif ant['direction'] == self.WEST:
                    ant['x'] -= 1
                
                ant['x'] %= self.WIDTH
                ant['y'] %= self.HEIGHT

                self.changed_tiles.append((ant['x'], ant['y']))

            self.board = next_board
    
    def display_board(self):
        for x, y in self.changed_tiles:
            goto(x, y)
            if self.board.get((x, y), False):
                bg(self.BLACK_TILE)
            else:
                bg(self.WHITE_TILE)

            ant_is_here = False
            for ant in self.ants:
                if (x, y) in (ant['x'], ant['y']):
                    ant_is_here = True
                    if ant['direction'] == self.NORTH:
                        print(self.ANT_UP, end='')
                    elif ant['direction'] == self.SOUTH:
                        print(self.ANT_DOWN, end='')
                    if ant['direction'] == self.WEST:
                        print(self.ANT_RIGHT, end='')
                    elif ant['direction'] == self.EAST:
                        print(self.ANT_LEFT, end='')
                    break

            if not ant_is_here:
                print(' ', end='')

            goto(0, self.HEIGHT)
            bg(self.WHITE_TILE)
            print('Press CTRL-C to quit.', end='')

            stdout.flush()
            sleep(self.PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        sim = LangtonsAnt()
        sim.display_intro()
        sim.main()
    except KeyboardInterrupt:
        clear()
        exit()