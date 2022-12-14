'''
constants:
    HANGMAN_PICS
    WORDS:              words to choose from for each round
attributes:
    won
    correct_letters
    incorrect_letters
    player_guess
functions
    has_won:            check if player won
    draw_hangman:       draw current game state
    main:               main game logic
    get_player_guess:   player's guess
'''

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
        self.won = True
        self.correct_letters = []
        self.incorrect_letters = []
        self.player_guess = ''
    
    def display_intro(self):
        pass

    def has_won(self):
        pass

    def has_lost(self):
        pass

    def draw_hangman(self):
        pass

    def get_player_guess(self):
        pass