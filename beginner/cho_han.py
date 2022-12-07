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

    def game(self):
        pass        