class GuessTheNumber:
    NUMBER_OF_GUESSES = 10
    def __init__(self):
        self.guesses_left = self.NUMBER_OF_GUESSES
        self.correct_guess = None
        self.current_guess = None
    
    def display_intro(self):
        print('--------------------------------------------------------------')
        print('---------------------- Guess the Number ----------------------')
        print('--------------------------------------------------------------')
        print()
        print('I am thinking of a number between 1 and 100.')
        print()
    
    def main(self):
        pass