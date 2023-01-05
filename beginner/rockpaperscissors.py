from random import randint
from time import sleep
from sys import exit

class RockPaperScissors:
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    def __init__(s):
        s.wins = 0
        s.losses = 0
        s.ties = 0
        s.player_move = None
        s.computer_move = None
    
    def get_player_move(s):
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit.')
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
            else:
                print('Enter one of R, P, S or Q.')

    def judge_round(s):
        if s.player_move == s.computer_move:
            s.ties += 1
            return 0
        elif s.player_move == s.ROCK and s.computer_move == s.SCISSORS:
            s.wins += 1
            return 1
        elif s.player_move == s.PAPER and s.computer_move == s.ROCK:
            s.wins += 1
            return 1
        elif s.player_move == s.SCISSORS and s.computer_move == s.PAPER:
            s.wins += 1
            return 1
        elif s.computer_move == s.ROCK and s.player_move == s.SCISSORS:
            s.losses += 1
            return -1
        elif s.computer_move == s.PAPER and s.player_move == s.ROCK:
            s.losses += 1
            return -1
        elif s.computer_move == s.SCISSORS and s.player_move == s.PAPER:
            s.losses += 1
            return -1

    def get_computer_move(s):
        random_number = randint(1, 3)
        if random_number == 1:
            s.computer_move = s.ROCK
        elif random_number == 2:
            s.computer_move = s.PAPER
        elif random_number == 3:
            s.computer_move = s.SCISSORS
    
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
    
    def display_computer_move(s):
        sleep(0.5)
        for i in range(3):
            print('{}...'.format(i+1))
            sleep(0.25)
        print(s.computer_move)
        sleep(0.5)
    
    def display_intro(s):
        print('Rock, Paper, Scissors')
        print('- Rock beats scissors.')
        print('- Paper beats rock.')
        print('- Scissors beats paper.')