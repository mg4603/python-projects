from random import randint
from time import sleep
from sys import exit

class RockPaperScissors:
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    def __init__(s):
        s.wins = 0
        s.losses = 0
        s.ties = 0