from random import choice
from time import sleep
from sys import exit

try:
    from playsound import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program.')
    print('use: python3 -m pip install playsound')
    exit()


class SoundMimic:
    PAUSE = 1
    def __init__(s):
        pass

    def display_intro(s):
        print('Sound Mimic')
        print('Try to memorize a patter of A S D F letters (each')
        print('with its own sound) as it gets longer and longer.')
        print()
    
    def play_letter(s, letter):
        playsound('sound{}.wav'.format(letter))
    
    def clear_terminal(s):
        print('\n' * 60)
    
