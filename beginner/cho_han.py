from random import randint
from sys import exit

class ChoHan:
    def __init__(self):
        self.money = 5000
        self.JAPANESE_NUMBERS = {
            1: 'ICHI', 
            2: 'NI',
            3: 'SAN',
            4: 'SHI',
            5: 'GO',
            6: 'ROKU'
        }

    def display_intro(self):
        print('------------------------------Cho-Han--------------------------')
        print()
        print('In this traditional Japanese dice game, two dice are rolled in ')
        print('a bamboo cup by the dealer sitting on the floor. The player')
        print('guess if the dice total to an even(cho) or odd(han) number.')
        print()

    def get_pot(self):
        print(f'You have {self.money} mon. How much do you bet? (or QUIT)')
        while True:
            pot = input('> ')
            if pot.upper() == 'QUIT':
                print('Thanks for playing!')
                exit()
            elif not pot.isdecimal():
                print('Please enter a positive number.')
            elif int(pot) > self.money:
                print('You don\'t have enough money to make that bet.')
            else:
                return int(pot)

    def get_bet(self):
        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks you for your bet.')
        while True:
            bet = input('> ').upper()
            if bet != 'CHO' and bet != 'HAN':
                print('Please enter either "CHO" OR "HAN".')
            else:
                return bet.lower()

    def handle_win(self, win_amt):
        self.money += win_amt
        print(f'You won! You take {win_amt} mon.')
        print(f'The house collects a {win_amt // 10} mon fee.')
        self.money -= (win_amt // 10)

    def game(self):
        while True:
            pot = self.get_pot()

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            bet = self.get_bet()

            print('The dealer lifts the cup to reveal:')
            print(f'    {self.JAPANESE_NUMBERS[dice1]}-{self.JAPANESE_NUMBERS[dice2]}')
            print(f'        {dice1}-{dice2}')

            is_even = (dice1 + dice2) % 2
            if is_even and bet == 'cho':
                self.handle_win(pot)
            elif not is_even and bet == 'han':
                self.handle_win(pot)
            else:
                self.money -= pot
                print('You lost!')
            
            if self.money == 0:
                print('You have run out of money!')
                print('Thanks for playing!')
                exit()

if __name__ == '__main__':
    choHan = ChoHan()
    choHan.game()