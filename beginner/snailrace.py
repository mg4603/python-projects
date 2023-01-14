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
    START = 'START'
    FINISH = 'FINISH'
    LINE = '|'
    LONG_PAUSE = 1.5
    SHORT_PAUSE = 0.5

    def __init__(s):
        s.num_of_snails = 0
        s.snail_names = []
        s.snail_progress = {}
        s.sleeping_snails = {}

    def display_intro(s):
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
            s.sleeping_snails[name] = 0
    
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
    
    def display_board(s):
        print('\n' * 40)
        print(f'{s.START}{" " * (s.FINISH_LINE - len(s.START))}{s.FINISH}')
        print(f'|{" " * (s.FINISH_LINE - len(s.LINE))}|')
        for snail_name in range(s.snail_names):
            print(
                '{}{}'.format(
                    ' ' * s.snail_progress[snail_name],
                    snail_name[:s.MAX_NAME_LENGTH]
                )
            )
            print('{}@v'.format(
                '.' * s.snail_progress[snail_name]
            ), end='')
            if s.sleeping_snails[snail_name]:
                print('zzz')

    def is_sleeping(s, name):
        if s.sleeping_snails[name]:
            s.sleeping_snails -= 1
            return True
        else:
            return False
    
    def check_victory(s):
        winners = []
        for snail_name in s.snail_names:
            if s.snail_progress[snail_name] == s.FINISH_LINE:
                    winners.append(snail_name)
        
        if len(winners) > 0:
            if len(winners) == 1:
                exit('{} has won!'.format(winners[0]))
            else:
                exit('It\'s a tie between {}'.format(
                    ', '.join(winners)
                ))

    def main(s):
        s.display_intro()
        s.get_num_of_snails()
        s.get_snail_names()
        s.display_board()
        sleep(s.LONG_PAUSE)

        while True:
            s.check_victory()
            for i in range(randint(1, s.num_of_snails // 2)):
                speed_boost = randint(0, 10)
                chance_of_sleeping = randint(0, 10)
                random_snail_name = choice(s.snail_names)
                if chance_of_sleeping == 1:
                    s.sleeping_snails[random_snail_name] = randint(1, 4)
                if s.is_sleeping(random_snail_name):
                    continue                    
                if speed_boost == 1:
                    s.snail_progress[random_snail_name] += 4
                    continue
                s.snail_progress[random_snail_name] += 1
            
            if 'Alvin' in s.snail_progress:
                s.snail_progress['Alvin'] += 1
            sleep(s.SHORT_PAUSE)
            s.display_board()


if __name__ == '__main__':
    sim = SnailRace()
    sim.main()