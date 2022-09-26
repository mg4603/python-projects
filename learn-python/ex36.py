from sys import exit

prompt = "> "

def dead(reason):
    print("%s. Better luck next time!" % reason)
    exit(0)

def win(reason):
    print("Wow! %s was probably a good choice. You actually survived. How shocking!" % reason)
    exit(0)

def swimming_pool():
    print("""You are at the swimming pool.
    There is a stranger in swimming in the pool.
    Do you choose to have a swim or go to the jacuzzi?""")

    next = input(prompt)

    if("swim" in next):
        dead("You were drowned by the deranged stranger")
    elif("jacuzzi" in next):
        dead("You were eaten by the piranhas that some lunatics put in the jacuzzi")
    else:
        win(next)

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def gym():
    print("""You are at the gym.
    The entire gym is empty, almost as if it were cleared ahead of time.
    Do you want to have a cardio day and run on the treadmill or perhaps do
    some bench presses.""")

    next = input(prompt)

    if("cardio" in next or "run" in next):
        machine = input("Pick which treadmill you want to use.\n%s" % prompt)

        while(not(isNum(machine))):
            print("Man learn to type a number")
            machine = input("Pick which treadmill you want to use.\n%s" % prompt)
            
        machine = int(machine)
        if(not(machine == 1 or machine == 2)):
            win(machine)
        else:
            if(machine == 1):
                dead("The treadmill was rigged to shortcircuit the runner")
            else:
                dead("The treadmill was rigged to blow when the runner tried to stop")                
    elif("bench presses" in next):
        dead("The bar was slipped and fell, crushing your neck")
    else:
        win(next)

