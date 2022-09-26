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
    print("%s Good job!" % reason)
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


def bear_room():
    print("""There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?""")
    bear_moved = False

    while True:
        next = input(prompt)
        
        if(next == "take honey"):
            dead("The bear looks at you, then slaps your face off.")
        elif(next == "taunt bear" and not bear_moved):
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif(next == "taunt bear" and bear_moved):
            dead("The bear gets pissed off and chews your leg off.")
        elif(next == "open door" and bear_moved):
            gold_room()
        else:
            print("I've got no idea what that means.")

bear_room()