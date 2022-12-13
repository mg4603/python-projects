from pathlib import Path

class HackingGame:
    GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

    def __init__(self, file_name):
        try:
            with Path(file_name).open('w') as file:
                self.WORDS = file.readlines()
            self.WORDS = [word.strip().upper() for word in self.WORDS]
        except FileNotFoundError:
            print('File {} not found in current working dir'.format(
                file_name
            ))
    
    def display_intro(self):
        print('--------------------------------------------------------')
        print('------------------- Hacking Minigame -------------------')
        print('--------------------------------------------------------')
        print()
        print('Find the password in the computer\'s memory. You are ')
        print('given clues after each guess. For example if the ')
        print('secret password is MONITOR but the player guessed')
        print('CONTAIN, they are given the hint that 2 out of 7')
        print('letters were correct, because both MONITOR and')
        print('CONTAIN have the letters O and N in their 2nd and 3rd')
        print('letter. You get four guesses.\n')
        