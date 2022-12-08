from sys import exit

class Diamond:
    def __init__(self, size, filled):
        self.size = size
        self.filled = filled
    
    def display_intro(self):
        pass

    def draw(self):
        pass

def get_size():
    print('Enter the size of the diamond you want to draw (greater than 0). or QUIT.')
    while True:
        response = input('> ').strip()
        if response.upper() == 'QUIT':
            exit()
        elif not (response.isdecimal() and int(response) > 0):
            print('Size must be an integer greater than 0.')
        else:
            return int(response)

def get_filled():
    pass

if __name__ == '__main__':
    size = get_size()
    isFilled = get_filled()
    diamond = Diamond(size, isFilled)
    diamond.draw()