'''
constants:
    HANGMAN_PICS
    WORDS:              words to choose from for each round
attributes:
    won
    game_over
    correct_letters
    incorrect_letters
    player_guess
functions
    has_won:            check if player won
    draw_hangman:       draw current game state
    main:               main game logic
    get_player_guess:   player's guess
'''
from random import choice

class Hangman:
    WORDS = [
        'ANT', 'BABOON', 'BADGER', 'BAT', 'BEAR', 'BEAVER', 
        'CAMEL', 'CAT', 'CLAM', 'COBRA', 'COUGAR', 'COYOTE', 'CROW',
        'DEER', 'DOG', 'DONKEY', 'DUCK', 'EAGLE', 
        'FERRET', 'FOX', 'FROG',
        'GOAT', 'GOOSE',
        'HAWK',
        'LION', 'LIZARD', 'LLAMA', 
        'MOLE', 'MONKEY', 'MOOSE', 'MOUSE', 'MULE',
        'NEWT', 
        'OTTER', 'OWL',
        'PANDA', 'PARROT', 'PIGEON', 'PYTHON',
        'RABBIT', 'RAM', 'RAT', 'RAVEN', 'RHINO', 
        'SALMON', 'SEAL', 'SHARK', 'SHEEP', 'SKUNK', 'SLOTH', 'SNAKE', 
        'SPIDER', 'STORK', 'SWAN',
        'TIGER', 'TOAD', 'TROUT', 'TURKEY', 'TURTLE', 
        'WEASEL', 'WHALE', 'WOLF', 'WOMBAT',
        'ZEBRA'
    ]
    HANGMAN_PICS = [
        r'''
        +--+
           |
           |
           |
           |
           |
       =====''',
        r'''
        +--+
        |  |
           |
           |
           |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
           |
           |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
        |  |
           |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
       /|  |
           |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
       /|\ |
           |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
       /|\ |
       /   |
           |
       =====''',
        r'''
        +--+
        |  |
        O  |
       /|\ |
       / \ |
           |
       =====''']

    def __init__(self):
        self.game_over = False
        self.won = False
        self.correct_letters = []
        self.incorrect_letters = []
        self.player_guess = ''
        self.secret_word = ''
    
    def display_intro(self):
        print('---------------------------------------------------')
        print('--------------------- Hangman ---------------------')
        print('---------------------------------------------------')

    def has_won(self):
        if self.game_over and self.won:
            return True

    def has_lost(self):
        if self.game_over and not self.won:
            return True

    def update_status(self):
        if ''.join(self.correct_letters) == self.secret_word:
            self.won = True
            self.game_over = True
            return 

        if len(self.incorrect_letters) == len(self.HANGMAN_PICS) - 1:
            self.game_over = True

    def draw_hangman(self):
        pass

    def get_player_guess(self):
        print('Guess a letter.')
        while True:
            guess = input('> ').upper()
            if len(guess) != 1:
                print('Please enter a single letter.')
                continue
            elif guess in self.correct_letters + self.incorrect_letters:
                print('You have already guessed that letter. Choose again.')
                continue
            elif not guess.isalpha():
                print('Please enter a LETTER.')
                continue
            else:
                self.player_guess = guess
                return
            

    def main(self):
        self.secret_word = choice(self.WORDS)

        while True:
            self.draw_hangman()
            self.get_player_guess()

            if self.player_guess in self.secret_word:
                self.correct_letters.append(self.player_guess)
            else:
                self.incorrect_letters.append(self.player_guess)
            
            self.update_status()

            if self.has_won():
                print('Yes! The secret word is: {}'.format(
                    self.secret_word
                ))
                print('You have won!')
                break
            elif self.has_lost():
                self.draw_hangman()
                print('You have run out of guesses!')
                print('The word was "{}".'.format(
                    self.secret_word
                ))
                break
