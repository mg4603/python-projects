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


def billiards_room():
    print("""You are at the billiards rooms.
    There are two gentlemen playing a game of snooker.
    Do you want to join in or play your own game.
    """)

    next = input(prompt)

    if("join" in next):
        dead("The gentleman that was losing, in a fit of misplaced rage,\
            \nkills you with his cue")
    elif("play" in next and "game" in next):
        dead("The gentlemen that was winning feels slighted that you didn't\
            \nask to join and together with his friend kills you and pins you\
            \nto the table")
    else:
        win(next)


def terrace():
    print("You are on the terrace.")
    dead("An out of control helicopter crashes into the terrace and dices you")

# def start():
