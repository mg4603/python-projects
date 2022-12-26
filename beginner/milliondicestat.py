from random import randint
from time import time

class MillionDiceSim:
    NUMBER_OF_SIMULATIONS = 1_000_000
    def __init__(self, number_of_dice, number_of_sides):
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides
        self.result = {}
        for i in range(
            self.number_of_dice, 
            (self.number_of_dice * self.number_of_sides + 1)
        ):
            self.result[i] = 0

    def display_results(s):
        print('TOTAL - ROLLS - PERCENTAGE')
        for i in range(
            s.number_of_dice, (s.number_of_dice * s.number_of_sides + 1)
        ):
            roll = s.result[i]
            percentage = round(s.result[i] / 10_000, 1)
        print('{} - {} rolls - {}'.format(i, roll, percentage))
    
    def simulate(s):
        print('Simulating 1,000,000 rolls of {} dice...'.format(
            s.number_of_dice
        ))
        last_print_time = time()
        for i in range(1_000_000):
            if time() > last_print_time + 1:
                print('{}% done...'.format(round(i/ 10_000, 1)))
                last_print_time = time()
            
            total = 0
            for i in range(s.number_of_dice):
                total += randint(1, s.number_of_sides)
            s.result[total] += 1
    
    def display_intro():
        print('--------------------------------------------------------')
        print('-------- Million Dice Roll Statistics Simulator --------')
        print('--------------------------------------------------------')
    
    def main(s):
        s.simulate()
        s.display_results()

def get_number_of_sides():
    print(
        'Enter the number of sides of dice whose roll you want to simulate'
    )
    while True:
        sides = input('> ')
        if is_int_gt_one(sides):
            return int(sides)
        print('Please enter an integer greater than 1')