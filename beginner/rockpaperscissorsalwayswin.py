from time import sleep
from sys import exit

class RockPaperScissors:
    LONG_PAUSE = 0.5
    SHORT_PAUSE = 0.25
    ROCK = 'ROCK'

    def __init__(s):
        s.wins = 0
        s.player_move = None
    
    def display_intro(s):
        print('Rock, Paper, Scissors')
        print('- Rock beats scissors.')
        print('- Rock crushes lizard.')
        print('- Paper wraps rock.')
        print('- Paper disproves spock.')
        print('- Scissor cuts paper.')
        print('- Scissor decapitates lizard.')
        print('- Lizard eats paper.')
        print('- Lizard poisons spock.')
        print('- Spock breaks scissors.')
        print('- Spock vaporizes rock.')
    
    def display_stats(s):
        print('Wins: {}, Losses: 0, Ties: 0'.format(s.wins))
    
