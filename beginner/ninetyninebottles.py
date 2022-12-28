from sys import exit
from time import sleep

class NinetyNineBottles:
    PAUSE = 2
    def __init__(s, bottles = 99):
        s.bottles = bottles
        assert s.bottles > 0

    def display_intro(s):
        print('Ninety-Nine Bottles')
        print()
        print('(Press CTRL-C to quit.)')
        print()
        sleep(2)
    
    def main(s):
        try:
            while s.bottles > 1:
                print('{} bottles of milk on the wall,'.format(s.bottles))
                sleep(s.PAUSE)
                print('{} bottles of milk,'.format(s.bottles))
                sleep(s.PAUSE)
                print('Take one down, pass it around,')
                sleep(s.PAUSE)
                s.bottles -= 1
                if s.bottles == 1:
                    print('1 bottle of milk on the wall!')
                    sleep(s.PAUSE)
                    print()
                    break
                print('{} bottles of milk on the wall!'.format(s.bottles))
                sleep(s.PAUSE)
                print()
            
            print('1 bottle of milk on the wall,')
            sleep(s.PAUSE)
            print('1 bottle of milk,')
            sleep(s.PAUSE)
            print('Take one down, pass it around,')
            sleep(s.PAUSE)
            print('No more bottles of milk on the wall!')
        except KeyboardInterrupt:
            exit()