from time import sleep
from sys import exit
from random import randint

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
        
    def display_moves(s):
        if s.player_move == s.ROCK:
            print('ROCK versus...')
        elif s.player_move == s.PAPER:
            print('PAPER versus...')
        elif s.player_move == s.SCISSORS:
            print('SCISSORS versus...')
        
        sleep(s.LONG_PAUSE)
        print('1...')
        sleep(s.SHORT_PAUSE)
        print('2...')
        sleep(s.SHORT_PAUSE)
        print('3...')
        print(s.SHORT_PAUSE)

        if s.player_move == s.ROCK:
            random_number = randint(1, 2)
            if random_number == 1:
                print('SCISSORS')
            elif random_number == 2:
                print('LIZARD')
        elif s.player_move == s.PAPER:
            random_number = randint(1, 2)
            if random_number == 1:
                print('SPOCK')
            elif random_number == 2:
                print('ROCK')
        elif s.player_move == s.SCISSORS:
            random_number = randint(1, 2)
            if random_number == 1:
                print('PAPER')
            elif random_number == 2:
                print('LIZARD')
        elif s.player_move == s.LIZARD:
            random_number = randint(1, 2)
            if random_number == 1:
                print('SPOCK')
            elif random_number == 2:
                print('PAPER')
        elif s.player_move == s.SPOCK:
            random_number = randint(1, 2)
            if random_number == 1:
                print('SCISSORS')
            elif random_number == 2:
                print('ROCK')
    
    def game(s):
        s.display_intro()
        while True:
            s.display_stats()
            s.get_player_move()
            s.display_moves()

            sleep(s.LONG_PAUSE)
            print('You win!')
            wins += 1