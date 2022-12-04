'''
- class Blackjack
    - methods:
        - intro
        - display_intro
        - play
- main
- runner code
'''

class Blackjack:
    def __init__(self):
        self.HEARTS = chr(9829)
        self.DIAMONDS = chr(9830)
        self.SPADES = chr(9824)
        self.CLUBS = chr(9827)
    
    def display_intro(self):
        print('''
Blackjack
The classic card game also known as 21. 
(This version doesn't have splitting or insurance.)

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On the first play, you can (D)ouble down to increase 
        your bet but you must hit exactly one more time before
        standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.

''')

    def play(self):
        pass

def main():
    blackjack = Blackjack()
    blackjack.display_intro()
    blackjack.play()

if __name__ == '__main__':
    main()