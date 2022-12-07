from random import randint
from copy import deepcopy
from time import sleep

class ConwaysGameOfLife:
    def __init__(self):
        self.WIDTH = 79
        self.HEIGHT = 20
        self.ALIVE = 'O'
        self.DEAD = ' '
        self.cells = {}
        self.next_cells = {}

    def simulate(self):
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if randint(0, 1) == 0:
                    self.next_cells[(x, y)] = self.ALIVE
                else:
                    self.next_cells[(x, y)] = self.DEAD
        
        while True:
            print('\n' * 50)
            self.cells = deepcopy(self.next_cells)

            for y in range(self.HEIGHT):
                for x in range(self.WIDTH):
                    print(self.cells[(x, y)], end='')
                print()
            
            print('Press CTRL-C to quit.')

            for x in range(self.WIDTH):
                for y in range(self.HEIGHT):
                    left = (x - 1) % self.WIDTH
                    right = (x + 1) % self.WIDTH
                    above = (y - 1) % self.HEIGHT
                    below = (y + 1) % self.HEIGHT

                    num_neighbors = 0
                    if self.cells[(left, above)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(x, above)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(right, above)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(left, y)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(right, y)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(left, below)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(x, below)] == self.ALIVE:
                        num_neighbors += 1
                    if self.cells[(right, below)] == self.ALIVE:
                        num_neighbors += 1
                    
                    if self.cells[(x, y)] == self.ALIVE and \
                        (num_neighbors == 2 or num_neighbors == 3):
                            self.next_cells[(x, y)] = self.ALIVE
                    elif self.cells[(x, y)] == self.DEAD and \
                        num_neighbors == 3:
                            self.next_cells[(x, y)] = self.ALIVE
                    else:
                        self.next_cells[(x, y)] = self.DEAD

            try:
                sleep(1)
            except KeyboardInterrupt:
                print('Conway\'s Game of Life')
                print()
                exit()

if __name__ == '__main__':
    game = ConwaysGameOfLife()
    game.simulate()