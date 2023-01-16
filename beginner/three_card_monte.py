from random import choice, shuffle
from time import sleep
class ThreeCardMonte:
    DELAY = 0.8
    NUM_OF_SWAPS = 16

    HEARTS = chr(9829)
    DIAMONDS = chr(9830)
    SPADES = chr(9824)
    CLUBS = chr(9827)

    LEFT = 0
    MIDDLE = 1
    RIGHT = 2

    def __init__(s):
        s.cards = [
            ('Q', s.HEARTS), s._get_random_card(), s._get_random_card()
        ]
        shuffle(s.cards)

    def _get_random_card(s):
        while True:
            suit = choice([s.HEARTS, s.CLUBS, s.DIAMONDS, s.SPADES])
            rank = choice(list('123456789JQKA') + ['10'])
    
            if suit == s.HEARTS and rank == 'Q':
                continue

            return (rank, suit)

    def has_won(s, guess):
        if s.cards[guess] == ('Q', s.HEARTS):
            return True
        return False

    def display_cards(s):
        rows = ['', '', '', '']
        for i, card in enumerate(s.cards):
            rows[0] = '___'
            rows[1] = '|{} |'.format(card[0].rjust(2))
            rows[2] = '| {} |'.format(card[1])
            rows[3] = '|_{}|'.format(card[0].rjust(2, '_'))
        
        for i in range(5):
            print(rows[i])
    
    def simulate_swaps(s):
        for _ in range(s.NUM_OF_SWAPS):
            swap = choice(['l-m', 'l-r', 'm-l', 'm-r', 'r-l', 'r-m'])

            if swap == 'l-m':
                print('swapping left and middle...', end='')
                s.cards[s.LEFT], s.cards[s.MIDDLE] = \
                    s.cards[s.MIDDLE], s.cards[s.LEFT]
            elif swap == 'l-r':
                print('swapping left and right...', end='')
                s.cards[s.LEFT], s.cards[s.RIGHT] = \
                    s.cards[s.RIGHT], s.cards[s.LEFT]
            elif swap == 'm-l':
                print('swapping middle and left...', end='')
                s.cards[s.MIDDLE], s.cards[s.LEFT] = \
                    s.cards[s.LEFT], s.cards[s.MIDDLE]
            elif swap == 'm-r':
                print('swapping middle and right...', end='')
                s.cards[s.MIDDLE], s.cards[s.RIGHT] = \
                    s.cards[s.RIGHT], s.cards[s.MIDDLE]
            elif swap == 'r-l':
                print('swapping right and left...', end='')
                s.cards[s.RIGHT], s.cards[s.LEFT] = \
                    s.cards[s.LEFT], s.cards[s.RIGHT]
            elif swap == 'r-m':
                print('swapping right and medium...', end='')
                s.cards[s.RIGHT], s.cards[s.MIDDLE] = \
                    s.cards[s.MIDDLE], s.cards[s.RIGHT]
            print('\r')
            sleep(s.DELAY)

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

    if game.has_won(guess):
        exit('You won!\nThanks for playing.')
    else:
        exit('You lost!\nThanks for playing.')

if __name__ == '__main__':
    main()