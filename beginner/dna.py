from time import sleep

class DnaAnimation:
    def __init__(self):
        self.PAUSE = 0.15
        self.ROWS = [
            #123456789
            '         ##',
            '        #{}-{}#',
            '       #{}---{}#',
            '     #{}-----{}#',
            '    #{}------{}#',
            '   #{}------{}#',
            '   #{}-----{}#',
            '    #{}---{}#',
            '    #{}-{}#',
            '      ##',
            '     #{}-{}#',
            '     #{}---{}#',
            '    #{}-----{}#',
            '    #{}------{}#',
            '     #{}------{}#',
            '      #{}-----{}#',
            '       #{}---{}#',
            '        #{}-{}#'
            #123456789
        ]
        

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('------------------------DNA Animation------------------------')
        print('-------------------------------------------------------------')
        print('A simple animation of a DNA double-helix.')
        print('Press CTRL-C to quit...')
        print()
        sleep(2)

    def animate(self):
        pass

if __name__ == '__main__':
    animator = DnaAnimation()
    animator.display_intro()
    animator.animate()