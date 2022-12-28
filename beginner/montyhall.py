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
        s.swap_wins = 0
        s.swap_losses = 0
        s.stay_wins = 0
        s.stay_losses = 0
        s.door_pick = None
        s.swap = None

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
    
    def display_results(s):
        total_swaps = s.swap_losses + s.swap_wins
        if total_swaps != 0:
            swap_success = round(s.swap_wins / total_swaps * 100, 1)
        else:
            swap_success = 0.0
        
        total_stays = s.stay_losses + s.stay_wins
        if total_stays != 0:
            stay_success = round(s.stay_wins / total_stays * 100, 1)
        else:
            stay_success = 0.0
        
        print()
        print('Swapping:     ', end='')
        print('{} wins, {} losses, '.format(
            s.swap_wins, s.swap_losses
        ), end='')
        print('success rate {}%'.format(swap_success))
        print('Not Swapping: ', end='')
        print('{} wins, {} losses, '.format(
            s.stay_wins, s.stay_losses
        ), end='')
        print('success rate {}%'.format(stay_success))
        print()
    
    def get_door_pick(s):
        while True:
            print('Pick a door 1, 2, or 3 (or "quit" to stop):')
            response = input('> ').upper()
            if response == 'QUIT':
                exit('Thanks for playing!')
            
            if response == '1' or response == '2' or response == '3':
                return int(response)
    
    def get_swap(s):
        while True:
            print('Do you want to swap doors? Y/N')
            swap = input('> ').upper()
            if swap == 'Y' or swap == 'N':
                s.swap = swap
                return
            

    def main(s):
        door_that_has_car = randint(1, 3)

        s.display_doors(
            s.DOOR_CLOSED_ONE, s.DOOR_CLOSED_TWO, s.DOOR_CLOSED_THREE
        )
        s.get_door_pick()

        while True:
            show_goat_door = randint(1, 3)
            if show_goat_door != s.door_pick and\
                    show_goat_door != door_that_has_car:
                break
        
        if show_goat_door == 1:
            s.display_doors(
                s.GOAT_DOOR, s.DOOR_CLOSED_TWO, s.DOOR_CLOSED_THREE
            )
        elif show_goat_door == 2:
            s.display_doors(
                s.DOOR_CLOSED_ONE, s.GOAT_DOOR, s.DOOR_CLOSED_THREE
            )
        elif show_goat_door == 3:
            s.display_doors(
                s.DOOR_CLOSED_ONE, s.DOOR_CLOSED_TWO, s.GOAT_DOOR
            )
        
        print('Door {} contains a goat!'.format(show_goat_door))

        s.get_swap()

        if s.swap == 'Y':
            if s.door_pick == 1 and show_goat_door == 2:
                s.door_pick = 3
            elif s.door_pick == 3 and show_goat_door == 2:
                s.door_pick = 1
            elif s.door_pick == 2 and show_goat_door == 3:
                s.door_pick = 1
            elif s.door_pick == 1 and show_goat_door == 3:
                s.door_pick = 2
            elif s.door_pick == 2 and show_goat_door == 1:
                s.door_pick = 3
            elif s.door_pick == 3 and show_goat_door == 1:
                s.door_pick = 2
        
        if door_that_has_car == 1:
            s.display_doors(
                s.CAR_DOOR, s.GOAT_DOOR, s.GOAT_DOOR
            )
        elif door_that_has_car == 2:
            s.display_doors(
                s.GOAT_DOOR, s.CAR_DOOR, s.GOAT_DOOR
            )
        elif door_that_has_car == 3:
            s.display_doors(
                s.GOAT_DOOR, s.GOAT_DOOR, s.CAR_DOOR
            )
        
        print('Door {} has the car!'.format(door_that_has_car))

        if s.door_pick == door_that_has_car:
            print('You won!')
            if s.swap == 'Y':
                s.swap_wins += 1
            elif s.swap == 'N':
                s.stay_losses += 1
        else:
            print('You lost!')
            if s.swap == 'Y':
                s.swap_losses += 1
            elif s.swap == 'N':
                s.stay_losses += 1

if __name__ == '__main__':
    game = MontyHall()
    game.display_intro()
    try:
        while True:
            game.main()
            game.display_results()
            input('Press Enter to continue or CTRL-C to quit.')
    except KeyboardInterrupt:
        exit('Thanks for playing!') 