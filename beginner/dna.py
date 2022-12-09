from time import sleep
from sys import exit
from random import randint

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
        try:
            row_index = 0
            while True:
                row_index += 1
                if row_index == len(self.ROWS):
                    row_index = 0
                
                if row_index == 0 or row_index == 9:
                    print(self.ROWS[row_index])
                    continue
                
                # select random nucleotide pairs:
                #   guanine-cytosine
                #   adenine-thymine
                random_selection = randint(1, 4)
                if random_selection == 1:
                    left_nucleotide, right_nucleotide = 'A', 'T'
                elif random_selection == 2:
                    left_nucleotide, right_nucleotide = 'T', 'A'
                elif random_selection == 3:
                    left_nucleotide, right_nucleotide = 'C', 'G',
                elif random_selection == 4:
                    left_nucleotide, right_nucleotide = 'G', 'C'

                print(self.ROWS[row_index].format(left_nucleotide, right_nucleotide))
                sleep(self.PAUSE)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    animator = DnaAnimation()
    animator.display_intro()
    animator.animate()