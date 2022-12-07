from sevseg import SevSeg

class Countdown:
    def __init__(self, hours, mins, secs, message):
        self.hours, self.mins, self.secs = hours, mins, secs
        self.message = message
    
    def display_intro(self):
        pass