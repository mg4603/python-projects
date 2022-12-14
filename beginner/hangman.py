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
    def __init__(self):
        self.won = True
        self.correct_letters = []
        self.incorrect_letters = []
        self.player_guess = ''
