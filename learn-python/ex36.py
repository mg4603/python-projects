from sys import exit

def dead(reason):
    print("You died by %s. Better luck next time!" % reason)
    exit(0)

def win():
    print("Wow! You actually survived. How shocking!")
    exit(0)


def 