'''
const:
    ITEMS
    SUSPECTS
    PLACES
    TIME_TO_SOLVE
    PLACE_FIRST_LETTERS
    LONGEST_PLACE_NAME_LENGTH       
attributes:
    visited_places:                 {}
    accused_suspects
    liars
    accusations_left
    culprit
    current_location
    clues
    zophie_clues
    known_suspects
    known_items
methods:
    display_intro
    get_clues
    get_room
    get_player_response
    main
'''

from random import randint, choice, shuffle
from sys import exit
from time import time

class Jaccuse:
    SUSPECTS = [
        'DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
        'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 
        'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON'
    ]
    ITEMS = [
        'FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 
        'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 
        'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD'
    ]
    def __init__(self):
        pass