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
        pass