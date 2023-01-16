from copy import copy
from sys import exit

class TowerOfHanoi:
    TOTAL_DISKS = 5
    COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))
    def __init__(s):
        s.towers = {'A': copy(s.COMPLETE_TOWER), 
                    'B': [],
                    'C': []}
        

    def display_towers(s):
        pass

    def _display_disk(s):
        pass

    def check_won(s):
        pass

    def make_move(s):
        pass

def display_intro():
    print('The Tower of Hanoi')
    print()
    print('Move the tower of disks, one disk at a time, to another target.')
    print('Larger disks cannot rest on top of a smaller disk.')

def main():
    game = TowerOfHanoi()
    display_intro()
    while True:
        game.display_towers()

        print('Enter the letters of "from" and "to" towers, or QUIT.')
        move = input('> ').upper().strip()

        if move == 'QUIT':
            exit()
        
        if not game.make_move():
            print('Invalid move!')
            continue

        if game.check_won():
            print('You have solved the puzzle! Well done!')
            exit('Thanks for playing.')

if __name__ == '__main__':
    main()