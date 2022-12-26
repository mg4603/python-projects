from random import randint
from time import time

class MillionDiceSim:
    NUMBER_OF_SIMULATIONS = 1_000_000
    def __init__(self, number_of_dice, number_of_sides):
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides
