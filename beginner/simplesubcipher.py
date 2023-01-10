from random import shuffle
try:
    from pyperclip import copy
except ImportError:
    pass

class SubCipher:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(s, key):
        s.key = key
    
    def display_intro(s):
        print('Simple Substitution Cipher')
        print('A simple substitution cipher has one-to-one translation')
        print('for each symbol in plaintext and each symbol in the cipher')
        print('text.')


