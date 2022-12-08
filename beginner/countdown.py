from sevseg import SevSeg

class Countdown:
    def __init__(self, hours, mins, secs, message):
        self.hours, self.mins, self.secs = hours, mins, secs
        self.message = message
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('--------------------------Countdown--------------------------')
        print('-------------------------------------------------------------')
        print('Show a countdown timer animation using a seven-segment ')
        print('display.')
        print('Requires sevseg to be in the same folders')
        print('Press CTRL-C to stop.')
        print()
    
    def main(self):
        pass