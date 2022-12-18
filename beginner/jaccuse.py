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
    known_suspects_and_items
methods:
    display_intro
    get_clues
    get_room
    get_player_response
    main
'''

from random import randint, choice, shuffle, sample
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
    PLACES = [
        'ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 
        'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 
        'ALBINO ALLIGATOR PIT'
    ]
    TIME_TO_SOLVE = 300
    PLACE_FIRST_LETTERS = {}
    LONGEST_PLACE_NAME_LENGTH = 0
    def __init__(self):
        for place in self.PLACES:
            self.PLACE_FIRST_LETTERS[place[0]] = place
            if len(place) > self.LONGEST_PLACE_NAME_LENGTH:
                self.LONGEST_PLACE_NAME_LENGTH = len(place)
        
        assert len(self.SUSPECTS) == 9
        assert len(self.PLACES) == 9
        assert len(self.SUSPECTS) == 9
        assert len(self.LONGEST_PLACE_NAME_LENGTH.keys()) == len(self.PLACES)
        self.known_suspects_and_items = []
        self.clues = {}
        self.zophie_clues = {}
        self.accusations_left = 3
        self.visited_places = {}
        self.accused_suspects = []
        
        shuffle(self.SUSPECTS)
        shuffle(self.PLACES)
        shuffle(self.ITEMS)

        self.liars = sample(self.SUSPECTS, randint(3, 4))
        self.current_location = 'TAXI'
        self.culprit = choice(self.SUSPECTS)

    def display_intro(self):
        print('-----------------------------------------------------------')
        print('------------------------ J\'ACCUSE ------------------------')
        print('-----------------------------------------------------------')
        print('Inspired by Homestar Runner\'s "Where\'s an Egg?" game')
        print()
        print('You are the world-famous detective Mathilde Camus.')
        print('ZOPHIE THE CAT has gone missing, and you must sift through')
        print('the clues.')
        print('Suspects either always tell lies, or tell the truth. Ask')
        print('them about other people, places, and items to see if the ')
        print('details they give are truthful and consistent with your')
        print('observations. Then you will know if their clue about')
        print('ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE CAT')
        print('in time and accuse the other party?')
        print()
        