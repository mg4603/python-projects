class HexGrid:
    X_REPEAT = 19
    Y_REPEAT = 12
    def __init__(self):
        pass
    
    def main(self):
        for y in range(self.Y_REPEAT):
            for x in range(self.X_REPEAT):
                print('/ \\_', end='')
            print()
            for x in range(self.X_REPEAT):
                print('\_/ ', end='')
            print()

if __name__ == '__main__':
    grid = HexGrid()
    grid.main()