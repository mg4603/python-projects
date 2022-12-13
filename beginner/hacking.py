from pathlib import Path
from random import choice
from sys import exit

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
        
        self.game_words = []
        self.computer_memory = ''
        self.secret_password = ''
        self.player_guess = ''
        self.num_matches = 0
    
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
    
    def main(self):
        input('Press Enter to begin...')
        self.get_game_words()
        self.get_computer_memory_string()
        self.secret_password = choice(self.game_words)

        print(self.computer_memory)
        for tries_remaining in range(4, 0, -1):
            print('Enter password: ({} tries remaining)'.format(
                tries_remaining
            ))
            self.get_player_guess()
            if self.player_guess == self.secret_password:
                print('A C C E S S  G R A N T E D')
                return
            else:
                self.get_num_matching_letters()
                print('Access Denied ({}/7 correct)'.format(
                    self.num_matches
                ))
        print('Out of tries. Secret password was {}.'.format(
            self.secret_password
        ))