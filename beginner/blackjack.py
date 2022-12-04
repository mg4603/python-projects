'''
- class Blackjack
    - methods:
        - intro                 #
        - display_intro         #
        - play                  #
        - get_bet               /
        - get_deck              /
        - display_hands(bool)   /
        - get_hand_value        /
        - get_player_hand_value /
        - get_dealer_hand_value /
        - get_move              /
        
- main                          #
- runner code                   #
'''
from sys import exit

class Blackjack:
    def __init__(self):
        self.HEARTS = chr(9829)
        self.DIAMONDS = chr(9830)
        self.SPADES = chr(9824)
        self.CLUBS = chr(9827)
        self.BACKSIDE = 'backside'
        self.money = 5000
        self.player_hand = []
        self.dealer_hand = []
    
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

    def get_deck(self):
        pass

    def get_bet(self, max_bet):
        pass

    def display_hands(self, show_dealer_hand):
        pass

    def get_hand_value(self):
        pass

    def get_player_hand_value(self):
        pass

    def get_dealer_hand_value(self):
        pass

    def get_move(self):
        pass

    def play(self):
        while True:
            if self.money <= 0:
                print('You\'re broke!')
                print('Good thing you weren\'t playing with real money.')
                print('Thanks for playing!')
                exit()
            
            print(f'Money: {self.money}')
            bet = self.get_bet(self.money)

            deck = self.get_deck()
            self.dealer_hand = [deck.pop(), deck.pop()]
            self.player_hand = [deck.pop(), deck.pop()]

            print(f'Bet: {bet}')
            # keep looping until player stands or busts
            # bust: value of cards over 21
            while True:
                self.display_hands(False)
                
                if self.get_player_hand_value() > 21:
                    break
                
                move = self.get_move(bet)

                if move == 'D':
                    # doubling down: player can increase bet
                    additional_bet = self.get_bet(min(bet, (self.money - bet)))
                    bet += additional_bet
                    print(f'Bet increased to {bet}.')
                    print(f'Bet: {bet}')

                if move in ('H', 'D'):
                    new_card = deck.pop()
                    rank, suit = new_card
                    print(f'You drew a {rank} of {suit}.')
                    self.player_hand.append(new_card)
                
                    if self.get_player_hand_value() > 21:
                        # the player has busted
                        continue
                
                if move in ('S', 'D'):
                    break
            
            if self.get_player_hand_value() <= 21:
                while self.get_dealer_hand_value() < 17:
                    print('Dealer hits...')
                    self.dealer_hand.append(deck.pop())
                    self.display_hands(False)

                    if self.get_dealer_hand_value() > 21:
                        break
                    input('Press Enter to continue...')
                    print('\n\n')
            
            self.display_hands(True)

            player_value = self.get_player_hand_value()
            dealer_value = self.get_dealer_hand_value()

            if dealer_value > 21:
                print(f'Dealer busts! You win ${bet}!')
                money += bet
            elif (player_value > 21) or (player_value < dealer_value):
                print('You lost!')
                money -= bet
            elif player_value > dealer_value:
                print(f'You won ${bet}!')
                money += bet
            elif player_value == dealer_value:
                print('It\'s a tie, the bet is returned to you.')
            
            input('Press Enter to continue...')
            print('\n\n')


def main():
    blackjack = Blackjack()
    blackjack.display_intro()
    blackjack.play()

if __name__ == '__main__':
    main()