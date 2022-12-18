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
    setup_clues
    setup_zophie_clues
    get_room_response             player response in a particular room
    get_taxi_response             player response when in taxi
    get_time_left
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
        self.known_suspects = []
        self.known_items = []
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
        self.start_time = None
        self.end_time = None

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
    
    def setup_clues(self):
        assert len(self.liars) > 0

        for i, interviewee in enumerate(self.SUSPECTS):
            if interviewee not in self.liars:
                self.clues[interviewee] = {}
                self.clues[interviewee]['debug_liar'] = False
                for item in self.ITEMS:
                    if randint(0, 1) == 0:
                        self.clues[interviewee][item] = \
                            self.PLACES[self.ITEMS.index(item)]
                    else:
                        self.clues[interviewee][item] = \
                            self.SUSPECTS[self.ITEMS.index(item)]
                for suspect in self.SUSPECTS:
                    if randint(0, 1) == 0:
                        self.clues[interviewee][suspect] = \
                            self.PLACES[self.ITEMS.index(suspect)]
                    else:
                        self.clues[interviewee][suspect] = \
                            self.ITEMS[self.ITEMS.index(suspect)]
            
            else:
                self.clues[interviewee] = {}
                self.clues[interviewee]['debug_liar'] = True
                for item in self.ITEMS:
                    if randint(0, 1) == 0:
                        while True:
                            self.clues[interviewee][item] = \
                                choice(self.PLACES)
                            if self.clues[interviewee][item] !=\
                                    self.PLACES[self.ITEMS.index(item)]:
                                break
                    else:
                        while True:
                            self.clues[interviewee][item] = \
                                choice(self.SUSPECTS)
                            if self.clues[interviewee][item] !=\
                                    self.SUSPECTS[self.ITEMS.index(item)]:
                                break

                for suspect in self.SUSPECTS:
                    if randint(0, 1) == 0:
                        while True:
                            self.clues[interviewee][suspect] =\
                                choice(self.PLACES)
                            if self.clues[interviewee][suspect] !=\
                                    self.PLACES[self.SUSPECTS.index(suspect)]:
                                break
                    else:
                        while True:
                            self.clues[interviewee][suspect] = \
                                choice(self.ITEMS)
                            if self.clues[interviewee][suspect] !=\
                                    self.ITEMS[self.SUSPECTS.index(suspect)]:
                                break
    
    def setup_zophie_clues(self):
        assert self.culprit != ''
        for interviewee in sample(self.SUSPECTS, randint(3, 4)):
            kind_of_clue = randint(1, 3)
            if kind_of_clue == 1:
                if interviewee not in self.liars:
                    self.zophie_clues[interviewee] = self.culprit
                elif interviewee in self.liars:
                    while True:
                        self.zophie_clues[interviewee] = \
                            choice(self.SUSPECTS)
                        if self.zophie_clues[interviewee] !=\
                                self.culprit:
                            break

            elif kind_of_clue == 2:
                if interviewee not in self.liars:
                    self.zophie_clues[interviewee] = \
                        self.PLACES[self.SUSPECTS.index(self.culprit)]
                elif interviewee in self.liars:
                    while True:
                        self.zophie_clues[interviewee] =\
                            choice(self.PLACES)
                        if self.zophie_clues[interviewee] !=\
                                self.PLACES[self.SUSPECTS.index(self.culprit)]:
                            break

            elif kind_of_clue == 3:
                if interviewee not in self.liars:
                    self.zophie_clues[interviewee] =\
                        self.ITEMS[self.SUSPECTS.index(self.culprit)]
                elif interviewee in self.liars:
                    while True:
                        self.zophie_clues[interviewee] =\
                            choice(self.ITEMS)
                        if self.zophie_clues[interviewee] !=\
                                self.ITEMS[self.SUSPECTS.index(self.culprit)]:
                            break

    def get_time_left(self):
        assert self.end_time is not None
        print()
        minutes_left = int(self.end_time - time()) // 60
        secs_left = int(self.end_time - time()) % 60
        print('Time left: {} mins, {} secs'.format(
            minutes_left, secs_left
        ))
    
    def get_room_response(self):
        print()
        print(
            '(J) "J\'ACCUSE!" ({} accusations left)'.format(
                self.accusations_left
            )
        )
        print('(Z) Ask if they know where ZOPHIE THE CAT is.')
        print('(T) Go back to the TAXI.')
        for i, suspect in enumerate(self.known_suspects):
            print('({}) Ask about {}'.format(
                i + 1, suspect
            ))
        for i, item in enumerate(self.known_items):
            print('({}) Ask about {}'.format(
                i + len(self.known_suspects),
                item
            ))

        while True:
            response = input('> ').upper()
            if response in 'JZT' or \
                    (
                        response.isdecimal() and 
                        0 < int(response) <= (len(self.known_items) + len(self.known_suspects))
                    ):
                break
        return response

    def get_taxi_response(self):
        if self.current_location == 'TAXI':
            print('You are in your TAXI. Where do you want to go?')
            for place in sorted(self.PLACES):
                place_info = ''
                if place in self.visited_places:
                    place_info = self.visited_places[place]
                name_label = '({}){}'.format(place[0], place[1:])
                spacing = ' ' * (self.LONGEST_PLACE_NAME_LENGTH - len(place))
                print('{} {}{}'.format(
                    name_label, spacing, place_info
                ))
            print('(Q)UIT GAME')
            while True:
                response = input('> ').upper()
                if response == '':
                    continue
                elif response == 'Q':
                    exit('Thanks for playing!')
                elif response in self.PLACE_FIRST_LETTERS.keys():
                    break
            self.current_location = self.PLACE_FIRST_LETTERS[response]
            return

    def check_lost(self):
        assert self.end_time
        if time() > self.end_time or self.accusations_left == 0:
            if time() > self.end_time:
                exit_msg = 'You have run out of time!\n'
            elif self.accusations_left == 0:
                exit_msg = 'You have accused too many innocent people!'

            culprit_index = self.SUSPECTS.index(self.culprit)
            exit_msg += \
                'It was {} at {} with the {} that catnapped her!\n'.format(
                    self.culprit, self.PLACES[culprit_index], 
                    self.ITEMS[culprit_index]
                )
            exit_msg += 'Better luck next time, Detective.'
            exit(exit_msg)

    def process_room(self):
        print('     You are at the {}.'.format(
                self.current_location
            ))
        current_location_index = self.PLACES.index(self.current_location)
        the_person_here = self.SUSPECTS[current_location_index]
        the_item_here = self.ITEMS[current_location_index]
        print('     {} with the {} is here.'.format(
            the_person_here, the_item_here
        ))

        if the_person_here not in self.known_suspects:
            self.known_suspects.append(the_person_here)
        if the_item_here not in self.known_items:
            self.known_items.append(the_item_here)
        if self.current_location not in self.visited_places.keys():
            self.visited_places[self.current_location] = \
                '({}, {})'.format(
                    the_person_here.lower(), the_item_here.lower()
                )
        
        if the_person_here in self.accused_suspects:
            print('They are offended that you accused them,')
            print('and will not help with your investigation.')
            print('You go back to your TAXI.')
            print()
            input('Press Enter to continue...')
            self.current_location = 'TAXI'
        
        response = self.get_room_response()

        if response == 'J':
            self.accusations_left -= 1
            if the_person_here == self.culprit:
                exit_msg = 'You\'ve cracked the case, Detective!'
                exit_msg += 'It was {} who had catnapped ZOPHIE THE CAT.'.format(
                    self.culprit
                )
                exit_msg += 'Good job! You solved it in {} min, {}sec.'.format(
                    *self.time_taken()
                )
                exit(exit_msg)
            else:
                self.accused_suspects.append(the_person_here)
                msg = 'You have accused the wrong person, Detective!'
                msg += 'They will not help you with anymore clues.'
                msg += 'You go back to your TAXI.'
                self.current_location = 'TAXI'
                print(msg)
        elif response == 'Z':
            if the_person_here not in self.zophie_clues:
                msg = '"I don\'t know anything about ZOPHIE THE CAT."'
            elif the_person_here in self.zophie_clues:
                msg = '     They give you this clue: "{}"'.format(
                    self.zophie_clues[the_person_here]
                )
                if self.zophie_clues[the_person_here] not in self.PLACES:
                    if(
                        self.zophie_clues[the_person_here] in self.ITEMS and 
                        self.zophie_clues[the_person_here] not in self.known_items
                    ):
                        self.known_items.append(self.zophie_clues[the_person_here])
                    if(
                        self.zophie_clues[the_person_here] in self.SUSPECTS and
                        self.zophie_clues[the_person_here] not in self.known_suspects
                    ):
                        self.known_suspects.append(self.zophie_clues[the_person_here])
            print(msg)
        elif response == 'T':
            self.current_location = 'TAXI'
        else:
            response = int(response)
            is_item = False
            if response >= len(self.known_items):
                thing_being_asked_about \
                    = self.known_suspects[response - len(self.known_items)]
            else:
                is_item = True
                thing_being_asked_about = self.known_items[response]
            
            if thing_being_asked_about in (the_person_here, the_item_here):
                clue = '     They give you this clue: "No comment."'
            else:
                clue = '     They give you this clue: {}'
                clue = clue.format(
                    self.clues[the_person_here][thing_being_asked_about]
                )
                if self.clues[the_person_here][thing_being_asked_about] \
                        not in self.PLACES:
                    if is_item:
                        if self.clues[the_person_here][thing_being_asked_about]\
                                not in self.known_items:
                            self.known_items.append(
                                self.clues[the_person_here][thing_being_asked_about]
                            )
                    else:
                        if self.clues[the_person_here][thing_being_asked_about]\
                                not in self.known_suspects:
                            self.known_suspects.append(
                                self.clues[the_person_here][thing_being_asked_about]
                            )
            print(clue)

    def time_taken(self):
        assert self.start_time
        minutes_taken = int(time() - self.start_time) // 60
        secs_taken = int(time() - self.start_time) % 60
        return minutes_taken, secs_taken

