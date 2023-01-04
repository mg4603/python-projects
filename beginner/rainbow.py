from time import sleep
from sys import exit
try:
    from bext import fg
except ImportError:
    exit('This program requires the bext module.')

class Rainbow:
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    INDIGO = 'cyan'
    VIOLET = 'purple'

    def __init__(s):
        s.indent = 0
        s.indent_increasing = True

    def display_intro(s):
        print('Rainbow')
        print('Press CTRL-C to stop.')
        sleep(3)
    
    def main(s):
        while True:
            print(' ' * s.indent, end='')
            fg(s.RED)
            print('##', end='')
            fg(s.YELLOW)
            print('##', end='')
            fg(s.GREEN)
            print('##', end='')
            fg(s.BLUE)
            print('##', end='')
            fg(s.INDIGO)
            print('##', end='')
            fg(s.VIOLET)
            print('##', end='')
            print()

            if s.indent_increasing:
                s.indent += 1
                if s.indent == 60:
                    s.indent_increasing = False
            else:
                s.indent -= 1
                if s.indent == 0:
                    s.indent_increasing = True
            
            sleep(0.02)
            