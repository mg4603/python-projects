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

def sandwich_cost(
            bread, protein, want_cheese, cheese, want_mayo, 
            want_mustard, want_lettuce, want_tomato):
    cost = 0
    cost += choose_bread(bread)
    cost += choose_protein(protein)
    if want_cheese == 'yes':
        cost += choose_cheese(cheese)
    if want_mayo == 'yes':
        cost += 1
    if want_mustard == 'yes':
        cost += 1
    if want_lettuce == 'yes':
        cost += 0.5
    if want_tomato == 'yes':
        cost += 0.5
    return cost

if __name__ == '__main__':
    # Using inputMenu() for a bread type: wheat, white, or sourdough.
    bread = inputMenu(
        prompt='What type of bread do you want in your sandwich?\n',
        choices=['wheat', 'white', 'sourdough']
    )
    
    # Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
    protein = inputMenu(
        prompt='What type of protein do you want in your sandwich?\n',
        choices=['chicken', 'turkey', 'ham', 'tofu']
    )

    # Using inputYesNo() to ask if they want cheese.
    want_cheese = inputYesNo(
        prompt='Do you want cheese in your sandwich\n'
    )

    cheese = ''
    if want_cheese == 'yes':
        # If so, using inputMenu() to ask for a cheese type: cheddar,
        # Swiss or mozzarella.
        cheese = inputMenu(
            prompt='What type of cheese do you want in your sandwich?\n',
            choices=['cheddar', 'Swiss', 'mozzarella']
        )

    want_mayo = inputYesNo(
        prompt='Do you want mayo in your sandwich?\n'
    )

    want_mustard = inputYesNo(
        prompt='Do you want mustard in your sandwich?\n'
    )

    want_lettuce = inputYesNo(
        prompt='Do you want lettuce in your sandwich?\n'
    )

    want_tomato = inputYesNo(
        prompt='Do you want tomato in your sandwich?\n'
    )
    
    num_of_sandwiches = inputInt(
        prompt="How many sandwiches do you want?\n",
        min=1
    )

    print(
        'Cost of sandwich: %s' %
        (
            num_of_sandwiches * sandwich_cost(
                bread, protein, want_cheese, cheese, want_mayo, 
                want_mustard, want_lettuce, want_tomato
            )
        )
    )