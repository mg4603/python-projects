from sys import exit
from random import randint
from time import sleep

class NinetyNineBottles2:
    def __init__(s, bottles = 99):
        s.bottles = bottles
    


if __name__ == '__main__':
    obj = NinetyNineBottles2()
    obj.display_intro()
    try:
        obj.main()
    except KeyboardInterrupt:
        exit()