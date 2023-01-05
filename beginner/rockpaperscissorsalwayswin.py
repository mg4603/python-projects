from time import sleep
from sys import exit

class RockPaperScissors:
    LONG_PAUSE = 0.5
    
    def __init__(s):
        s.wins = 0
        s.player_move = None