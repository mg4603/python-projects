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
        for level in range(s.TOTAL_DISKS, -1, -1):
            for tower in s.towers.keys():
                if level >= len(s.towers[tower]):
                    s._display_disk(0)
                else:
                    s._display_disk(s.towers[tower][level])
            print()
        
        empty_spaces = s.TOTAL_DISKS * ' '
        print('{0} A{0}{0} B{0}{0} C\n'.format(empty_spaces))

    def _display_disk(s, width):
        num_empty_spaces = s.TOTAL_DISKS - width
        empty_spaces = ' ' * num_empty_spaces
        if width == 0:
            print('{}||{}'.format(empty_spaces, empty_spaces), end='')
        else:
            print('{}{}{}{}{}'.format(
                empty_spaces, '@' * width, str(width).rjust(2, '_'),
                '@' * width, empty_spaces
            ), end='')

    def check_won(s):
        if s.COMPLETE_TOWER in (s.towers['B'], s.towers['C']):
            return True
        return False

    def make_move(s, move):
        if move not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            return False
        
        from_tower, to_tower = move
        if not len(s.towers[from_tower]) > 0:
            return False
        elif len(s.towers[to_tower]) == 0:
            disk = s.towers[from_tower].pop()
            s.towers[to_tower].append(disk)
            return True
        elif s.towers[to_tower][-1] < s.towers[from_tower][-1]:
            return False
        else:
            disk = s.towers[from_tower].pop()
            s.towers[to_tower].append(disk)
            return True

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
        
        if not game.make_move(move):
            print('Invalid move!')
            continue

        if game.check_won():
            print('You have solved the puzzle! Well done!')
            exit('Thanks for playing.')

if __name__ == '__main__':
    main()