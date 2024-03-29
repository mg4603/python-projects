from random import shuffle

class Bagel:
    def __init__(self):
        self.NUM_DIGITS = 3
        self.MAX_GUESSES = 10

    def print_banner(self):
        print(f'''
####################################   Bagels    ####################################

I am thinking of a {self.NUM_DIGITS}-number with no repeated digits. Try to guess
what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct but in the right position.
    Bagels      No digit is correct.

For example, if the secret number was 248 and your guess was 843, the clues would be:
    Fermi Pico.
''')

    def get_secret_number(self):
        numbers = list('0123456789')
        shuffle(numbers)

        secret_num = ''
        for i in range(self.NUM_DIGITS):
            secret_num += str(numbers[i])
        return secret_num
        
    def get_clues(self, guess, secret_num):
        if guess == secret_num:
            return 'You got it!'

        clues = []

        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                clues.append('Fermi')
            elif guess[i] in secret_num:
                clues.append('Pico')
        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return ' '.join(clues)

    def game(self):
        self.print_banner()
        secret_num = self.get_secret_number()
        print('I have thought of up a number.')
        print(f'You have {self.MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while True:
            while num_guesses <= self.MAX_GUESSES:
                guess = ''
                while len(guess) != self.NUM_DIGITS or not guess.isdecimal():
                    print(f'Guess #{num_guesses}')
                    guess = input('> ')
    
                clues = self.get_clues(guess, secret_num)
                print(clues)
                num_guesses += 1
    
                if guess == secret_num:
                    break
                if num_guesses > self.MAX_GUESSES:
                    print('You ran out of guesses')
                    print(f'The answer was {secret_num}')
                
            print('Do you want to play again? (yes/no)')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playing')

def main():
    bagel = Bagel()
    bagel.game()


if __name__ == '__main__':
    main()