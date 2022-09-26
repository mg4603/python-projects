from multiprocessing.sharedctypes import Value
from sys import exit

prompt = "> "

def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def dead(reason):
    print("%s Good job!")
    exit(0)

def win(reason):
    print("%s, you win!" % reason)
    exit(0)

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input(prompt)
    if(isNum(next)):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    
    if(how_much  < 50):
        win("Nice, you're not greedy")
    else:
        dead("You greedy bastard!")

gold_room()