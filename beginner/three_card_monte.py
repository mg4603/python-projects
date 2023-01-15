from random import choice

class ThreeCardMonte:
    DELAY = 0.8
    NUM_OF_SWAPS = 16

    HEARTS = chr(9829)
    DIAMONDS = chr(9830)
    SPADES = chr(9824)
    CLUBS = chr(9827)

    LEFT = 0
    
    def __init__(s):
        pass

    def get_random_card(s):
        pass

    def has_won(s, guess):
        pass

    def display_cards(s):
        pass
    
    def simulate_swaps(s):
        pass
    
def display_intro():
    print('Three-Card Monte')
    print()
    print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
    print('the cards move.')
    print()

def get_guess():
    while True:
        print('Make your guess? (LEFT, RIGHT, MIDDLE)')
        guess = input('> ').upper()

        if guess == 'LEFT':
            return 0
        elif guess == 'MIDDLE':
            return 1
        elif guess == 'RIGHT':
            return 2
        
        print('Invalid guess.')
        print()

def main():
    display_intro()
    input('Press Enter to begin...')

    game = ThreeCardMonte()
    
    print('Here are the cards:')
    game.display_cards()

    game.simulate_swaps()
    print('\n' * 60)

    guess = get_guess()

    game.has_won(guess)

if __name__ == '__main__':
    main()