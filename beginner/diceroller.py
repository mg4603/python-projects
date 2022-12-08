class DiceRoller:
    def __init__(self):
        pass

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