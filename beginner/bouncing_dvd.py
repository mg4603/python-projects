from sys import exit
try:
    from bext import goto, size
except:
    print('This program requires the bext module, which')
    print('you can install by following the instructions')
    print('at https://pypi.org/project/bext')
    exit()

class BouncingDvd:
    def __init__(self):
        self.WIDTH, self.HEIGHT = size()

    def animate(self):
        pass

def main():
    bouncingDvd = BouncingDvd()
    bouncingDvd.animate()

if __name__ == '__main__':
    main()