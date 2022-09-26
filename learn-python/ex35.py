from multiprocessing.sharedctypes import Value
from sys import exit

prompt = "> "

def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input(prompt)
    if(isNum(next)):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    
    if(how_much  < 50):
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
