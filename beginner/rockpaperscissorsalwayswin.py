from time import sleep
from sys import exit

class RockPaperScissors:
    LONG_PAUSE = 0.5
    SHORT_PAUSE = 0.25
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'
    LIZARD = 'LIZARD'
    SPOCK = 'SPOCK'

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
    
    def get_player_move(s):
        print('{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}\n\t{}'.format(
            'Enter your move:',
            '(R)ock',
            '(P)aper',
            '(S)cissors',
            '(L)izard',
            '(Sp)ock',
            '(Q)uit'
        ))
        while True:
            response = input('> ').upper()
            if response == 'Q':
                exit('Thanks for playing!')
            elif response == 'R':
                s.player_move = s.ROCK
                return
            elif response == 'P':
                s.player_move = s.PAPER
                return
            elif response == 'S':
                s.player_move = s.SCISSORS
                return
            elif response == 'L':
                s.player_move = s.LIZARD
                return
            elif response == 'SP':
                s.player_move = s.SPOCK
                return
            else:
                print('Type one of R, P, S, Sp or Q.')