from random import randint
from time import sleep
from sys import exit

class RockPaperScissors:
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'
    LIZARD = 'LIZARD'
    SPOCK = 'SPOCK'

    def __init__(s):
        s.wins = 0
        s.losses = 0
        s.ties = 0
        s.player_move = None
        s.computer_move = None
    
    def get_player_move(s):
        print(
            '{}{}'.format(
                'Enter your move: (R)ock (P)aper (S)cissors,', 
                ' (L)izard, (Sp)ock or (Q)uit.')
        )
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
                print('Enter one of R, P, S or Q.')

    def judge_round(s):
        if s.player_move == s.computer_move:
            s.ties += 1
            return 0
        elif s.player_move == s.ROCK and s.computer_move == s.SCISSORS:
            s.wins += 1
            return 1
        elif s.player_move == s.ROCK and s.computer_move == s.LIZARD:
            s.wins += 1
            return 1
        elif s.player_move == s.PAPER and s.computer_move == s.ROCK:
            s.wins += 1
            return 1
        elif s.player_move == s.PAPER and s.computer_move == s.SPOCK:
            s.wins += 1
            return 1
        elif s.player_move == s.SCISSORS and s.computer_move == s.PAPER:
            s.wins += 1
            return 1
        elif s.player_move == s.SCISSORS and s.computer_move == s.LIZARD:
            s.wins += 1
            return 1
        elif s.player_move == s.LIZARD and s.computer_move == s.SPOCK:
            s.wins += 1
            return 1
        elif s.player_move == s.LIZARD and s.computer_move == s.PAPER:
            s.wins += 1
            return 1
        elif s.player_move == s.SPOCK and s.computer_move == s.SCISSORS:
            s.wins += 1
            return 1
        elif s.player_move == s.SPOCK and s.computer_move == s.ROCK:
            s.wins += 1
            return 1
        elif s.computer_move == s.ROCK and s.player_move == s.SCISSORS:
            s.losses += 1
            return -1
        elif s.computer_move == s.ROCK and s.player_move == s.LIZARD:
            s.losses += 1
            return 1
        elif s.computer_move == s.PAPER and s.player_move == s.ROCK:
            s.losses += 1
            return -1
        elif s.computer_move == s.PAPER and s.player_move == s.SPOCK:
            s.losses += 1
            return 1
        elif s.computer_move == s.SCISSORS and s.player_move == s.PAPER:
            s.losses += 1
            return -1
        elif s.computer_move == s.SCISSORS and s.player_move == s.LIZARD:
            s.losses += 1
            return 1
        elif s.computer_move == s.LIZARD and s.player_move == s.SPOCK:
            s.losses += 1
            return 1
        elif s.computer_move == s.LIZARD and s.player_move == s.PAPER:
            s.losses += 1
            return 1
        elif s.computer_move == s.SPOCK and s.player_move == s.SCISSORS:
            s.losses += 1
            return 1
        elif s.computer_move == s.SPOCK and s.player_move == s.ROCK:
            s.losses += 1
            return 1

    def get_computer_move(s):
        random_number = randint(1, 5)
        if random_number == 1:
            s.computer_move = s.ROCK
        elif random_number == 2:
            s.computer_move = s.PAPER
        elif random_number == 3:
            s.computer_move = s.SCISSORS
        elif random_number == 4:
            s.computer_move = s.LIZARD
        elif random_number == 5:
            s.computer_move = s.SPOCK
    
    def display_stats(s):
        print('Wins: {}, Losses: {}, Ties: {}'.format(
            s.wins, s.losses, s.ties
        ))
    
    def display_player_move(s):
        if s.player_move == s.ROCK:
            print('{} versus...'.format(s.ROCK))
        elif s.player_move == s.PAPER:
            print('{} versus...'.format(s.PAPER))
        elif s.player_move == s.SCISSORS:
            print('{} versus...'.format(s.SCISSORS))
        elif s.player_move == s.LIZARD:
            print('{} versus...'.format(s.LIZARD))
        elif s.player_move == s.SPOCK:
            print('{} versus...'.format(s.SPOCK))
    
    def display_computer_move(s):
        sleep(0.5)
        for i in range(3):
            print('{}...'.format(i+1))
            sleep(0.25)
        print(s.computer_move)
        sleep(0.5)
    
    def display_intro(s):
        print('Rock, Paper, Scissors, Lizard, Spock')
        print('- Rock breaks scissors.')
        print('- Rock crushes lizard.')
        print('- Paper wraps rock.')
        print('- Paper disproves spock.')
        print('- Scissors cuts paper.')
        print('- Scissors decapitates lizard.')
        print('- Lizard poisons spock.')
        print('- Lizard eats paper.')
        print('- Spock breaks scissors.')
        print('- Spock vaporizes rock.')

    def game(s):
        s.display_intro()
        while True:
            s.display_stats()
            s.get_player_move()
            s.display_player_move()
            s.get_computer_move()
            s.display_computer_move()
            round = s.judge_round()

            if round == 0:
                print('It\'s a tie!')
            elif round == 1:
                print('You win!')
            elif round == -1:
                print('You lose!')

if __name__ == '__main__':
    game = RockPaperScissors()
    try:
        game.game()
    except KeyboardInterrupt:
        exit()