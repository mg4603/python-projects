from random import randint
from sys import exit

class MontyHall:
    DOOR_CLOSED_ONE = '''
+------+
|      |
|      |
|   1  |
|      |
|      |
+------+
'''
    DOOR_CLOSED_TWO = '''
+------+
|      |
|      |
|   1  |
|      |
|      |
+------+
'''
    DOOR_CLOSED_THREE = '''
+------+
|      |
|      |
|   1  |
|      |
|      |
+------+
'''
    GOAT_DOOR = '''
+------+
|  ((  |
|  oo  |
| /_/|_|
|    | |
|GOAT|||
+------+
'''
    CAR_DOOR = '''
+------+
| CAR! |
|    __|
|  _/  |
| /_ __|
|   O  |
+------+
'''


    def __init__(s):
        pass

    def display_doors(s, door_one, door_two, door_three):
        door_one = door_one.splitlines()
        door_two = door_two.splitlines()
        door_three = door_three.splitlines()

        for i, line in enumerate(door_one):
            print('{}  {}  {}'.format(
                line, 
                door_two[i].strip(), 
                door_three[i].strip()
            ))
    
    def display_intro(s):
        print('------------------------------------------------------------')
        print('------------------ The Monty Hall Problem ------------------')
        print('------------------------------------------------------------')
        print()
        print('In the Monty Hall game show, you can pick one of three doors.')
        print('One door has a new car for a prize. The other two doors have')
        print('worthless goats:')
        s.display_doors(
            s.DOOR_CLOSED_ONE, s.DOOR_CLOSED_TWO, s.DOOR_CLOSED_THREE
        )
        print('Say you pick Door #1.')
        print('Before the door you choose is opened, another door with a')
        print('goat, is opened:')
        s.display_doors(
            s.DOOR_CLOSED_ONE, s.DOOR_CLOSED_TWO, s.GOAT_DOOR
        )
        print('You can choose to either open the door you originally picked')
        print('or swap to the other unopened door.')
        print()
        print('It may seem like it doesn\'t matter if you swap or not, but')
        print('your odds do improve if you swap doors! This program')
        print('demonstrates the Monty Hall problem by letting you do repeated')
        print('experiments.')
        print()
        input('Press Enter to stat...')
        