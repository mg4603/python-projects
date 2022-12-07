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
 _A_
|   |      Each digit is a seven-segment display:
F   B      _        _   _        _   _   _   _   _
|_G_|     | |   |   _|  _|  |_| |_  |_    | |_| |_|         
|   |     |_|   |  |_   _|    |  _| |_|   | |_|  _|
E   C
|_D_|''')

