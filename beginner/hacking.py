from pathlib import Path
from random import choice, sample, randint
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
    
    def get_game_words(self):

        # add three words that have zero matching letters
        while len(self.game_words) < 3:
            word = self.get_one_word_except(self.game_words)
            if self.get_num_matching_letters(word) == 0:
                self.game_words.append(word)
        
        # two words with 3 matching letters: only upto 500 tries
        for _ in range(500):
            word = self.get_one_word_except(self.game_words)
            if self.get_num_matching_letters(word) == 3:
                self.game_words.append(word)

            if len(self.game_words) == 5:
                break

        # seven words that have at least 1 matching letter
        for _ in range(500):
            word = self.get_one_word_except(self.game_words)
            if self.get_num_matching_letters(self.game_words) >= 1:
                self.game_words.append(word)
            
            if len(self.game_words) == 12:
                break
        
        while len(self.game_words) < 12:
            self.game_words.append(self.get_one_word_except(self.game_words))
        
        assert len(self.game_words) == 12
                
                

    def get_computer_memory_string(self):
        pass

    def get_player_guess(self):
        while True:
            guess = input('> ').upper()
            if guess in self.game_words:
                self.player_guess = guess
                return
            print('That is not one of the possible passwords listed above.')
            print('Try entering "{}" or "{}".'.format(
                self.game_words[0],
                self.game_words[1]
            ))

    def get_num_matching_letters(self, word2):
        matching_letters = 0
        for i in range(len(self.secret_password)):
            if self.secret_password[i] == word2[2]:
                matching_letters += 1
        
        return matching_letters

    def get_one_word_except(self, block_list=None):
        if block_list == None:
            block_list = []
        
        while True:
            word = choice(self.game_words)
            if word not in block_list:
                return word

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