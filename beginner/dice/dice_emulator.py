from random import randint
def roll():
    return randint(1, 6)
while True:
    while True:
        try:
            choice = input("Do you want to roll the dice?(Y/n)")
            if choice.lower() != 'y' and choice.lower() != 'n':
                raise(ValueError)
            else:
                break
        except ValueError:
            print("Enter a valid input")
            continue
        else:
            break
    if choice.lower() == 'n':
        break
    print(roll())
