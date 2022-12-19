'''
mapping
    'a': ['4', '@', '/-\\'],
    'c': ['('],
    'd': ['|)'],
    'e': ['3'],
    'f': ['ph'],
    'h': [']-[', '|-|'],
    'i': ['1', '!', '|'],
    'k': [']<'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7', '+'],
    'u': ['|_|'],
    'v': ['\\/']
'''
from random import random, choice
try:
    from pyperclip import copy, paste
except ImportError:
    pass

class LeetSpeak:
    CHAR_MAP = {
        'a': ['4', '@', '/-\\'],
        'c': ['('],
        'd': ['|)'],
        'e': ['3'],
        'f': ['ph'],
        'h': [']-[', '|-|'],
        'i': ['1', '!', '|'],
        'k': [']<'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7', '+'],
        'u': ['|_|'],
        'v': ['\\/']   
    }
    LEET_MAP = {
         '4': 'a',
         '@': 'a',
         '/-\\': 'a',
         '(': 'c',
         '|)': 'd',
         '3': 'e',
         'ph': 'f',
         ']-[': 'h',
         '|-|': 'h',
         '1': 'i',
         '!': 'i',
         '|': 'i',
         ']<': 'k',
         '0': 'o',
         '$': 's',
         '5': 's',
         '7': 't',
         '+': 't',
         '|_|': 'u',
         '\\/': 'v' 
    }

    def __init__(self):
        pass
    
    def display_intro(self):
        print('----------------------------------------------------')
        print('-------------- L3375P34]< (leetspeak) --------------')
        print('----------------------------------------------------')
          
    def english_to_leetspeak(self, msg):
        leetspeak = ''
        for char in msg:
            if char in self.CHAR_MAP and random() <= 0.7:
                leetspeak += choice(self.CHAR_MAP[char.lower()])
            else:
                leetspeak += char
        
        print(leetspeak)
        try:
            copy(leetspeak)
            print('(Copied leetspeak to clipboard).')
        except NameError:
            pass
    
    def leetspeak_to_english(self, leet_msg):
        english_msg = ''
        for char in self.LEET_MAP:
            while char in leet_msg:
                width = len(char)
                start = leet_msg.find(char)
                prev_msg = leet_msg
                leet_msg = '{}{}{}'.format(
                    prev_msg[: start],
                    self.LEET_MAP[char],
                    prev_msg[start + width:]
                )

        english_msg = leet_msg
        print(english_msg)
        try:
            copy(english_msg)
            print('(Copied english message to clipboard).')
        except NameError:
            pass

if __name__ == '__main__':
    print('Enter your leet message:')
    message = input('> ')
    print()
    leetEngine = LeetSpeak()
    leetEngine.english_to_leetspeak(message)
    leetEngine.leetspeak_to_english(paste())