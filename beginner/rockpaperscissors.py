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
            elif response in ('R', 'P', 'S'):
                s.player_move = response
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