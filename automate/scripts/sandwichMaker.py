"""
• Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
• Using inputInt() to ask how many sandwiches they want. Make sure this
number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.

"""
from pyinputplus import inputMenu, inputYesNo, inputInt

def choose_bread(bread):
    cost = 0
    if bread == 'wheat':
        cost = 2.5
    elif bread == 'white':
        cost = 2
    elif bread == 'sourdough':
        cost = 2.75
    else:
        raise Exception('Invalid bread type')
    return cost

def choose_protein(protein):
    if protein == 'chicken':
        return 2
    elif protein == 'turkey':
        return 2.35
    elif protein == 'ham':
        return 2.5
    elif protein == 'tofu':
        return 3.5
    else:
        raise Exception('Invalid protein type')

def choose_cheese(cheese):
    if cheese == 'cheddar':
        return 1
    elif cheese == 'swiss':
        return 1.5
    elif cheese == 'mozzarella':
        return 1.05
    else:
        raise Exception('Invalid cheese type')

