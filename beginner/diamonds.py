class Diamond:
    def __init__(self, size, filled):
        self.size = size
        self.filled = filled

def get_size():
    pass

def get_filled():
    pass

if __name__ == '__main__':
    size = get_size()
    isFilled = get_filled()
    diamond = Diamond(size, isFilled)
    diamond.draw()