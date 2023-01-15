from sys import exit

class Soroban:
    NUM_OF_DIGITS = 10

    def __init__(s):
        s.board = s.create_board()

    def create_board(s):
        seg_sep = f'+{"=" * 3 * s.NUM_OF_DIGITS}==+\n'
        board = seg_sep
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' 
        board += f'I {" | " * s.NUM_OF_DIGITS} I\n' 
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' 
        board += seg_sep
        board += f'I {" {} " * s.NUM_OF_DIGITS} I\n' * 6
        board += f'+{"=={}" * s.NUM_OF_DIGITS}==+'
        return board
    
    def display_controls(s):
        print('  +q w e r t y u i o p')
        print('  -a s d f g h j k l ;')
        print('(Enter a number, "quit", or a stream of up/down letters.)')

    def display_board(s, number):
        number_list = list(str(number).zfill(s.NUM_OF_DIGITS))

        has_bead = []
        
        # Top heaven row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # Bottom heaven row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 1st earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 2nd earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 3rd earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 4th earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 5th earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        # 6th earth row
        for i in range(s.NUM_OF_DIGITS):
            has_bead.append(number_list[i] in '012345679')

        abacus_chars = []
        for i, bead_present in enumerate(has_bead):
            if bead_present:
                abacus_chars.append('O')
            else:
                abacus_chars.append('|')
        chars = abacus_chars + number_list
        print(s.board.format(*chars))

    def get_commands(s):
        s.display_controls()
        absolute = False
        commands = input('> ')

        if commands == 'quit':
            exit()
        elif commands.isdecimal():
            absolute = True
            return int(commands), absolute
        else:
            number = 0
            for letter in commands:
                if letter == 'q':
                    number += 1_000_000_000
                elif letter == 'w':
                    number += 100_000_000
                elif letter == 'e':
                    number += 10_000_000
                elif letter == 'r':
                    number += 1_000_000
                elif letter == 't':
                    number += 100_000
                elif letter == 'y':
                    number += 10_000
                elif letter == 'u':
                    number += 1_000
                elif letter == 'i':
                    number += 100
                elif letter == 'o':
                    number += 10
                elif letter == 'p':
                    number += 1
                elif letter == 'a':
                    number -= 1_000_000_000
                elif letter == 's':
                    number -= 100_000_000
                elif letter == 'd':
                    number -= 10_000_000
                elif letter == 'f':
                    number -= 1_000_000
                elif letter == 'g':
                    number -= 100_000
                elif letter == 'h':
                    number -= 10_000
                elif letter == 'j':
                    number -= 1_000
                elif letter == 'k':
                    number -= 100
                elif letter == 'l':
                    number -= 10
                elif letter == ';':
                    number -= 1

            return number, absolute

    def display_intro(s):
        print('Soroban - The Japanese Abacus')
        print()
    
    def main(s):
        s.display_intro()

        abacus_number = 0
        while True:
            s.display_board(abacus_number)
            number, absolute = s.get_commands()
            if absolute:
                abacus_number = number
            else:
                abacus_number += number
                if abacus_number > 9_999_999_999:
                    abacus_number = 9_999_999_999
                if abacus_number < 0:
                    abacus_number = 0
