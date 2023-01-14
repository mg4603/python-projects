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
    FINISH_LINE = 40

    def __init__(s):
        s.num_of_snails = 0
        s.snail_names = []
        s.snail_progress = {}

    def display_intro():
        print('Snail Race')
        print('     @v <-- snail')
        print()
    
    def get_num_of_snails(s):
        while True:
            print('How many snails will race? Max: {}'.format(
                s.MAX_NUM_SNAILS
            ))
            response = input('> ')
            if response.isdecimal():
                s.num_of_snails = int(response)
                if 1 < s.num_of_snails <= s.MAX_NUM_SNAILS:
                    return
            print('Enter a number between 2 and {}'.format(
                s.MAX_NUM_SNAILS
            ))
    
    def get_snail_names(s):
        for i in range(s.num_of_snails):
            name = s.get_snail_name()
            s.snail_names.append(name)
            s.snail_progress[name] = 0
    
    def get_snail_name(s):
        while True:
            print('Enter snail #{}\' name:'.format(
                len(s.snail_names)
            ))
            name = input('> ')
            if len(name) == 0:
                print('Please enter a name.')
            elif name in s.snail_names:
                print('Choose a name that hasn\'t already been used.')
            else:
                return name
    
