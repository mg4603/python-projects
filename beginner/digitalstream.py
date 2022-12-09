from shutil import get_terminal_size

class DigitalStream:
    def __init__(self):
        self.MIN_STREAM_LENGTH = 6
        self.MAX_STREAM_LENGTH = 14
        self.PAUSE = 0.1
        self.STREAM_CHARS = ['0', '1']

        self.DENSITY = 0.2

        self.WIDTH = get_terminal_size()[0]
    
    def display_intro(self):
        print('--------------------------------------------------------------')
        print('------------------Digital Stream Screensaver------------------')
        print('--------------------------------------------------------------')
        print('Press CTRL-C to quit.')
        print()

    def animation(self):
        pass

if __name__ == '__main__':
    digital_stream = DigitalStream()
    digital_stream.display_intro()
    digital_stream.animation()