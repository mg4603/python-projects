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
        sleep(1)
        print('\n' * 60)
    
    def main(s):
        s.display_intro()
        input('Press Enter to begin...')
        pattern = ''
        while True:
            s.clear_terminal()
            pattern += choice('ASDF')

            print('Pattern: ', end='')
            for letter in pattern:
                print(letter, end=' ', flush=True)
                s.play_letter(letter)
            
            s.clear_terminal()

            print('Enter the pattern: ')
            response = input('> ').upper()

            if response != pattern:
                print('Incorrect!')
                print(f'The pattern was {pattern}')
            else:
                print('Correct!')
            
            for letter in pattern:
                s.play_letter(letter)
            
            if response != pattern:
                print(f'You scored {len(pattern) - 1} points.')
                exit('Thanks for playing!')

if __name__ == '__main__':
    game = SoundMimic()
    try:
        game.main()
    except KeyboardInterrupt:
        exit()