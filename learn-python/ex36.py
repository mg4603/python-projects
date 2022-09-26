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