from random import randint

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
    
    def get_secret_number(self):
        self.correct_guess = randint(1, 100)

    def get_guess(self):
        while True:
            response = input('> ').strip()
            if response.isdecimal() and 1 <= int(response) <= 100:
                self.current_guess = int(response)
                return
            print('Please enter a number between 1 and 100.')

    def main(self):
        self.get_secret_number()
        while True:
            print('You have {} guesses left. Take a guess.'.format(
                self.guesses_left
            ))
            self.get_guess()
            if self.current_guess == self.correct_guess:
                print('Yay! You guessed my number!')
                exit()
            elif self.current_guess < self.correct_guess:
                print('Your guess is too low.')
            elif self.current_guess > self.correct_guess:
                print('Your guess is too high.')
            
            self.guesses_left -= 1
            if self.guesses_left == 0:
                print('Game over. The number I was thinking of was {}'.format(
                    self.correct_guess
                ))

