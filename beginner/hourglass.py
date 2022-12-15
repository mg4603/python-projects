'''
constants:
    PAUSE_LENGTH:       time for which to pause between loop iteration
    WALL:               wall unicode
    SAND:               sand unicode
    X:                  key for tuple x value
    Y:                  key for tuple y value
    SCREEN_WIDTH:       screen width
    SCREEN_HEIGHT:      screen height
    WIDE_FALL_CHANCE:   Chance that sand falls wide(by two places instead of the normal 1)
    HOURGLASS:          set of co-ordinates that represent the hour glass
    INITIAL_SAND:       set of co-ordinates that represent the initial sand
attributes:
functions:
    display_intro
    main                main fn
    run_simulation:     change values
'''

from random import choice, shuffle, random
from sys import exit, stdout
from time import sleep

try:
    from bext import fg, clear, goto
except ImportError:
    print('This program requires the bext module to run.')
    print('Installation instructions can be found at')
    print('https://pypi.org/project/Bext')
    exit()

class HourGlass:
    PAUSE_LENGTH = 0.2
    WIDE_FALL_CHANCE = 50

    X = 0
    Y = 1

    SCREEN_WIDTH = 79
    SCREEN_HEIGHT = 25

    WALL = chr(9608)
    SAND = chr(9617)

    HOURGLASS = set()
    INITIAL_SAND = set()
    OUTSIDE_HOURGLASS = set()

    def __init__(self):
        for i in range(18, 37):
            self.HOURGLASS.add((i, 1))
            self.HOURGLASS.add((i, 23))
        
        for i in range(1, 5):
            self.HOURGLASS.add((18, i))
            self.HOURGLASS.add((36, i))
            self.HOURGLASS.add((18, i + 19))
            self.HOURGLASS.add((36, i + 19))

        for i in range(8):
            self.HOURGLASS.add((19 + i, 5 + i))
            self.HOURGLASS.add((35 - i, 5 + i))
            self.HOURGLASS.add((19 + i, 19 - i))
            self.HOURGLASS.add((35 - i, 19 - i))
        
        for i in range(self.SCREEN_WIDTH):
            self.OUTSIDE_HOURGLASS.add((i, 0))
            self.OUTSIDE_HOURGLASS.add((i, 23))
            self.OUTSIDE_HOURGLASS.add((i, 24))
            self.OUTSIDE_HOURGLASS.add((i, 25))
        
        for y in range(1, 5):
            for x in range(18):
                self.OUTSIDE_HOURGLASS.add((x, y))
                self.OUTSIDE_HOURGLASS.add((x, y + 19))
            for x in range(36, self.SCREEN_WIDTH):
                self.OUTSIDE_HOURGLASS.add((x, y))
                self.OUTSIDE_HOURGLASS.add((x, y + 19))

        for y in range(8):
            for x in range(19 + y):
                self.OUTSIDE_HOURGLASS.add((x, 5 + y))
                self.OUTSIDE_HOURGLASS.add((x, 19 - y))
            for x in range(36 - y, self.SCREEN_WIDTH):
                self.OUTSIDE_HOURGLASS.add((x, 5 + y))
                self.OUTSIDE_HOURGLASS.add((x, 19 - y))
        
        for y in range(8):
            for x in range(19 + y, 36 - y):
                self.INITIAL_SAND.add((x, y + 4))
        
        self.all_sand = []
    

    def display_intro(self):
        print('----------------------------------------------------')
        print('-------------------- Hour Glass --------------------')
        print('----------------------------------------------------')
        print()
        print('An animation of an hourglass with falling sand.')
        print('Press CTRL-C to stop.')
        print()
        sleep(2)
    
    def main(self):
        clear()

        goto(0, 0)
        fg('white')
        print('CTRL-C to quit.', end='')
        
        fg('black')
        for wall in self.HOURGLASS:
            goto(wall[self.X], wall[self.Y])
            print(self.WALL, end='')
        
        fg('yellow')
        while True:
            self.all_sand = list(self.INITIAL_SAND)
            for sand in self.all_sand:
                goto(sand[self.X], sand[self.Y])
                print(self.SAND, end='')
            
            self.run_simulation()

    def run_simulation(self):
        while True:
            shuffle(self.all_sand)

            sand_moved_on_this_step = False
            for i, sand in enumerate(self.all_sand):
                if sand[self.Y] == self.SCREEN_HEIGHT - 1:
                    continue
                
                below = (sand[self.X], sand[self.Y] + 1)
                no_sand_below = below not in self.all_sand
                no_wall_below = below not in self.HOURGLASS
                can_fall_down = no_wall_below and no_sand_below

                if can_fall_down:
                    goto(sand[self.X], sand[self.Y])
                    print(' ', end='')
                    goto(sand[self.X], sand[self.Y] + 1)
                    print(self.SAND, end='')

                    self.all_sand[i] = (sand[self.X], sand[self.Y] + 1)
                    sand_moved_on_this_step = True
                else:
                    below_left = (sand[self.X] - 1, sand[self.Y] + 1)
                    no_sand_below_left = below_left not in self.all_sand
                    no_wall_below_left = below_left not in self.HOURGLASS
                    left = (sand[self.X] - 1, sand[self.Y])
                    no_wall_left = left not in self.HOURGLASS
                    not_on_left_edge = sand[self.X] > 0
                    not_outside_hourglass = below_left not in self.OUTSIDE_HOURGLASS
                    
                    can_fall_left = (
                        no_sand_below_left and no_wall_left 
                            and no_wall_below_left and not_on_left_edge
                            and not_outside_hourglass
                    )
                    
                    below_right = (sand[self.X] + 1, sand[self.Y] + 1)
                    no_sand_below_right = below_right not in self.all_sand
                    no_wall_below_right = below_right not in self.HOURGLASS
                    right = (sand[self.X] + 1, sand[self.Y])
                    no_wall_right = right not in self.HOURGLASS
                    not_on_right_edge = sand[self.X] < self.SCREEN_WIDTH - 1
                    not_outside_hourglass = below_right not in self.OUTSIDE_HOURGLASS
                    can_fall_right = (
                        no_sand_below_right and no_wall_below_right
                        and no_wall_right and not_on_right_edge
                        and not_outside_hourglass
                    )

                    falling_direction = None
                    if can_fall_left and not can_fall_right:
                        falling_direction = -1
                    elif can_fall_right and not can_fall_left:
                        falling_direction = 1
                    elif can_fall_right and can_fall_left:
                        falling_direction = choice((-1, 1))
                    
                    if random() * 100 <= self.WIDE_FALL_CHANCE:
                        below_two_left = (sand[self.X] - 2, sand[self.Y] + 1)
                        no_sand_below_two_left = below_two_left not in self.all_sand
                        no_wall_below_two_left = below_two_left not in self.HOURGLASS
                        not_outside_hourglass = below_two_left not in self.OUTSIDE_HOURGLASS
                        not_on_second_to_left_edge = sand[self.X] > 1
                        can_fall_two_left = (
                            no_sand_below_two_left and no_wall_below_two_left
                            and not_on_second_to_left_edge and not_outside_hourglass
                        )

                        below_two_right = (sand[self.X] + 2, sand[self.Y] + 1)
                        no_sand_below_two_right = below_two_right not in self.all_sand
                        no_wall_below_two_right = below_two_right not in self.HOURGLASS
                        not_on_second_to_right_edge = sand[self.X] < self.SCREEN_WIDTH - 2
                        not_outside_hourglass = below_two_right not in self.OUTSIDE_HOURGLASS
                        can_fall_two_right = (
                            no_sand_below_two_right and no_wall_below_two_right
                            and not_on_second_to_right_edge and not_outside_hourglass
                        )

                        if can_fall_two_left and not can_fall_two_right:
                            falling_direction = -2
                        elif can_fall_two_right and not can_fall_two_left:
                            falling_direction = 2
                        elif can_fall_two_left and can_fall_two_right:
                            falling_direction = choice((-2, 2))
                    
                    if falling_direction == None:
                        continue
                    
                    goto(sand[self.X], sand[self.Y])
                    print(' ', end='')
                    goto(sand[self.X] + falling_direction, sand[self.Y] + 1)
                    print(self.SAND, end='')
                    self.all_sand[i] = (sand[self.X] + falling_direction, sand[self.Y] + 1)
                    sand_moved_on_this_step = True

            stdout.flush()
            sleep(self.PAUSE_LENGTH)

            if not sand_moved_on_this_step:
                sleep(2)
                for sand in self.all_sand:
                    goto(sand[self.X], sand[self.Y])
                    print(' ', end='')
                break

if __name__ == '__main__':
    try:
        hourglass = HourGlass()
        hourglass.main()
    except KeyboardInterrupt:
        clear()
        exit()