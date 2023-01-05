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