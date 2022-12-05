from sys import exit
try:
    from bext import goto
except:
    print('This program requires the bext module, which')
    print('you can install by following the instructions')
    print('at https://pypi.org/project/bext')
    exit()

class BouncingDvd:
    def __inti__(self):
        pass

    def animate(self):
        pass

def main():
    bouncingDvd = BouncingDvd()
    bouncingDvd.animate()

if __name__ == '__main__':
    main()