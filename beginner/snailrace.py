from sys import exit
from random import choice, randint
from time import sleep
'''
• Add a random “speed boost” that launches the snail four spaces ahead
instead of one.
• Add a “sleep mode” that snails can randomly enter during the race.
This mode causes them to stop for a few turns and zzz to appear next to
them.
• Add support for ties, in case snails reach the finish line at the same time
'''
class SnailRace:
    MAX_NUM_SNAILS = 8
    MAX_NAME_LENGTH = 20
    def __init__(s):
        pass