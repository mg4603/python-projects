class NumeralSystems:
    def __init__(s, start, amt):
        assert type(start) == int
        assert type(amt) == int
        s.start = start
        s.end = start + amt
        s.decimal_offset = len(str(s.end))
        s.bin_offset = len(str(bin(s.end)[2: ]))
        s.oct_offset = len(str(s.oct(s.end)[2: ]))
        s.hex_offset = len(str(hex(s.end)[2: ]))

    def oct(s, num):
        octal_number = ''
        while num > 0:
            octal_number = str(num % 8) + octal_number
            num //= 8
        return '0o' + octal_number


    def display_intro(s):
        print('-----------------------------------------------------------')
        print('----------------- Numeral System Counters -----------------')
        print('-----------------------------------------------------------')
        print()
        print('This program shows you equivalent numbers in decimal ')
        print('(base 10), hexadecimal (base 16), and binary (base 2) ')
        print('numeral systems.')
        print()
        print('(Ctrl-C to quit.)')
        print()
    
    def main(s):
        for num in range(s.start, s.end):
            bin_number = bin(num)[2:]
            oct_number = s.oct(num)[2:]
            hex_number = hex(num)[2:].upper()
            print('DEC: {}, HEX: {}, BIN: {}, OCT: {}'.format(
                str(num).rjust(s.decimal_offset),
                str(hex_number).rjust(s.hex_offset),
                str(bin_number).rjust(s.bin_offset),
                str(oct_number).rjust(s.oct_offset)
            ))

def get_whole_num(prompt, default):
    assert str(default).isdecimal(), 'Default value has to be a whole number'
    
    print(prompt)
    while True:
        response = input('> ')
        if response == '':
            return int(default)
        elif response.isdecimal():
            return int(response)

        print('Please enter a number greater than or equal to 0.')

if __name__ == '__main__':
    start = get_whole_num('Enter the starting number (e.g. 0)', 0)
    amt = get_whole_num('Enter how many numbers to display (e.g. 1000)', 1000)

    numeral_system = NumeralSystems(start, amt)
    numeral_system.display_intro()
    numeral_system.main()
