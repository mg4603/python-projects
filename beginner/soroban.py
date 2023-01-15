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

