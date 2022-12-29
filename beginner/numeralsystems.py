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
