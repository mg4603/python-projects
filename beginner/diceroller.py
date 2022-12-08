from sys import exit
from random import randint
class DiceRoller:
    def __init__(self):
        self.number_of_dice = 0
        self.number_of_sides = 0
        self.mod_amount = 0

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('-------------------------Dice Roller-------------------------')
        print('-------------------------------------------------------------')
        print()
        print('Enter what kind and how many dice to roll. The format is the ')
        print('number of dice, followed by "d", followed by the number of ')
        print('sides the dice have. You can also add a plus or minus ')
        print('adjustment.')
        print()
        print('Examples:')
        print('     3d6 rolls three 6-sided dice')
        print('     1d10+2 rolls one 10-sided die, and adds 2')
        print('     2d38-1 rolls two 38-sided die and and subtracts 1')
        print('     QUIT quits the program')

    def input_handler(self):
        dice_str = input('> ')
        if dice_str.upper() == 'QUIT':
            exit()

        # clean up dice_str
        dice_str = dice_str.lower().replace(' ', '')
        
        d_index = dice_str.find('d')
        if d_index == -1:
            raise Exception('Missing the "d" character.')
        
        # get number of dice
        number_of_dice = dice_str[:d_index]
        if not number_of_dice.isdecimal():
            raise Exception('Missing the number of dice.')
        self.number_of_dice = int(number_of_dice)

        mod_index = dice_str.find('+')
        if mod_index == -1:
            mod_index = dice_str.find('-')
        
        if mod_index == -1:
            number_of_sides = dice_str[d_index + 1:]
        else:
            number_of_sides = dice_str[d_index + 1: mod_index]
        
        if not number_of_sides.isdecimal():
            raise Exception('Missing number of sides.')
        self.number_of_sides = int(number_of_sides)

        # modifier amt
        if mod_index == -1:
            mod_amount = 0
        else:
            mod_amount = dice_str[mod_index + 1:]
            if not mod_amount.isdecimal():
                raise Exception('Missing modification amount')
            self.mod_amount = int(mod_amount)
            if dice_str[mod_index] == '-':
                self.mod_amount = -self.mod_amount
        
    def main(self):
        while True:
            try:
                self.input_handler()
                
                rolls = []
                for i in range(self.number_of_dice):
                    roll_result = randint(1, self.number_of_sides)
                    rolls.append(roll_result)
                
                print('Total: {} (Each die: '.format(sum(rolls) + self.mod_amount), end='')
                for i, roll in enumerate(rolls):
                    rolls[i] = str(roll)
                print(', '.join(rolls), end='')

                if self.mod_amount != 0:
                    if self.mod_amount > 0:
                        print(', +{}'.format(self.mod_amount), end='')
                print(')')

            except Exception as e:
                print('Invalid input. Enter something like "3d6" or "1d10+2".')
                print('     {}'.format(str(e)))
                continue

