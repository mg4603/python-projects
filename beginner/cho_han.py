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
                print('Please enter a number.')
            elif int(pot) > self.money:
                print('You don\'t have enough money to make that bet.')
            else:
                return int(pot)

    def get_bet(self):
        pass

    def game(self):
        while True:
            pot = self.get_pot()

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            bet = self.get_bet()

            is_even = (dice1 + dice2) % 2
            if is_even and bet == 'cho':
                print(f'You won! You take {pot} mon.')
                self.money += pot
                print(f'The house collects a {pot // 10} mon fee.')
                self.money -= (pot // 10)
            else:
                self.money -= pot
                print('You lost!')
            
            if self.money == 0:
                print('You have run out of money!')
                print('Thanks for playing!')
                exit()