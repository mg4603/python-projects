class Bagel:
    def __init__(self):
        NUM_DIGITS = 3
        MAX_GUESSES = 10

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


def main():
    pass

if __name__ == '__main__':
    main()