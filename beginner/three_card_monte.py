from random import choice

class ThreeCardMonte:
    def __init__(s):
        pass

    def get_random_card(s):
        pass

    def has_won(s, guess):
        pass

    def display_cards(s):
        pass

def display_intro():
    print('Three-Card Monte')
    print()
    print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
    print('the cards move.')
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