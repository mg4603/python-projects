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