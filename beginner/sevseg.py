class SevSeg:
    def __init__(self):
        pass

    def display_intro(self):
        print('--------------------------------------------------------------')
        print('----------------------------SevSeg----------------------------')
        print('A seven-segment number display module, used by the Countdown')
        print('and Digital Clock programs.')
        print()
        print(
'''A labeled seven-segment display, with each segment labeled A-G:
 __A__
|     |      Each digit is a seven-segment display:
F     B      __        __   __         __   __   __   __   __
|__G__|     |  |   |   __|  __|  |__| |__  |__     | |__| |__|         
|     |     |__|   |  |__   __|     |  __| |__|    | |__|  __|
E     C
|__D__|''')

    def get_sev_seg(self, number, min_width=0):
        number = str(number).zfill(min_width)

        rows = ['', '', '']
        for i, numeral in enumerate(number):
            if numeral == '.':
                rows[0] += ' '
                rows[1] += ' '
                rows[2] += '.'
                continue        #skip the space in between digits.
            elif numeral == '-':
                rows[0] += '    '
                rows[1] += ' __ '
                rows[2] += '    '
            elif numeral == '0':
                rows[0] += ' __ '
                rows[1] += '|  |'
                rows[2] += '|__|'
            elif numeral == '1':
                rows[0] += '    '
                rows[1] += '   |'
                rows[2] += '   |'
            elif numeral == '2':
                rows[0] += ' __ '
                rows[1] += ' __|'
                rows[2] += '|__ '
            elif numeral == '3':
                rows[0] += ' __ '
                rows[1] += ' __|'
                rows[2] += ' __|'
            elif numeral == '4':
                rows[0] += '    '
                rows[1] += '|__|'
                rows[2] += '   |'
            elif numeral == '5':
                rows[0] += ' __ '
                rows[1] += '|__ '
                rows[2] += ' __|'
            elif numeral == '6':
                rows[0] += ' __ '
                rows[1] += '|__ '
                rows[2] += '|__|'
            elif numeral == '7':
                rows[0] += ' __ '
                rows[1] += '   |'
                rows[2] += '   |'
            elif numeral == '8':
                rows[0] += ' __ '
                rows[1] += '|__|'
                rows[2] += '|__|'
            elif numeral == '9':
                rows[0] += ' __ '
                rows[1] += '|__|'
                rows[2] += ' __|'
            
            # add a space(in between numerals) if this isn't the last number
            if i != len(number) - 1:
                rows[0] += ' '
                rows[1] += ' '
                rows[2] += ' '
        
        return '\n'.join(rows)



