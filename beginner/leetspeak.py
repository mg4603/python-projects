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
    from pyperclip import copy
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
         ['4', '@', '/-\\']: 'a',
         ['(']: 'c',
         ['|)']: 'd',
         ['3']: 'e',
         ['ph']: 'f',
         [']-[', '|-|']: 'h',
         ['1', '!', '|']: 'i',
         [']<']: 'k',
         ['0']: 'o',
         ['$', '5']: 's',
         ['7', '+']: 't',
         ['|_|']: 'u',
         ['\\/']  : 'v' 
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
        return leetspeak
    
    def leetspeak_to_english(self, leet_msg):
        english_msg = ''
        for char in leet_msg:
            is_leet_char = False
            for key in self.LEET_MAP.keys():
                if char in key:
                    english_msg += self.LEET_MAP[key]
            
            if not is_leet_char:
                english_msg += char
        return english_msg

if __name__ == '__main__':
    print('Enter your leet message:')
    message = input('> ')
    print()
    leetEngine = LeetSpeak()
    leetEngine.english_to_leetspeak(message)