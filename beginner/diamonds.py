from sys import exit

class Diamond:
    def __init__(self, size, filled):
        self.size = size
        self.filled = filled
    
    def display_intro(self):
        print('----------------------------------------------------------------')
        print('----------------------------Diamonds----------------------------')
        print('----------------------------------------------------------------')
        print('Draw diamonds of various sizes')
        print()

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
    print('Should the diamond be filled or not? (YES/NO) or QUIT.')
    while True:
        response = input('> ').strip().upper()
        if response == 'QUIT':
            exit()
        elif not (response == 'YES' or response == 'NO'):
            print('Choice should be either YES or NO')
        else:
            if response == 'YES':
                return True
            else:
                return False

if __name__ == '__main__':
    size = get_size()
    isFilled = get_filled()
    diamond = Diamond(size, isFilled)
    diamond.draw()