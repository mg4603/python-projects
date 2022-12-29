class NumeralSystems:
    def __init__(s, start, amt):
        assert type(start) == int
        assert type(amt) == int
        s.start = start
        s.amt = amt
        s.decimal_offset = len(str(start + amt))
        s.bin_offset = len(str(bin(start + amt)))
        s.oct_offset = len(str(oct(start + amt)[2: ]))
        s.hex_offset = len(str(hex(start + amt)[2: ]))


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
