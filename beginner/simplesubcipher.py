from random import shuffle
try:
    from pyperclip import copy
except ImportError:
    pass

class SubCipher:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(s, message, key, mode):
        assert set(list(s.LETTERS)) == set(list(key)), \
                'There is an error in the key or symbol set.'
        s.key = key
        s.message = message
        s.mode = mode
    
    def display_intro(s):
        print('Simple Substitution Cipher')
        print('A simple substitution cipher has one-to-one translation')
        print('for each symbol in plaintext and each symbol in the cipher')
        print('text.')


    def translated_message(s, message, mode):
        translated = ''
        charset_a = s.LETTERS
        charset_b = s.key

        if mode == 'decrypt':
            charset_a, charset_b = charset_b, charset_b
        
        for symbol in message:
            if symbol.upper() in charset_a:
                idx = charset_a.find(symbol.upper())
                if symbol.isupper():
                    translated += charset_b[idx].upper()
                elif symbol.islower():
                    translated += charset_b[idx].lower()
            else:
                translated += symbol
        
        return translated
    
    def encrypt(s):
        return s.translated_message(s.message, 'encrypt')

    def decrypt(s):
        return s.translated_message(s.message, 'decrypt')
    
def check_key(key):
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if set(list(key)) == set(letters):
        return True
    else:
        return False

def generate_random_key():
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffle(letters)
    return ''.join(letters)

def get_key(mode):
    while True:
        print('Please specify the key to use.')
        if mode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            key = generate_random_key()
            print('The key is {}. KEEP THIS SECRET!'.format(key))
            return key
        else:
            if check_key(response):
                return response.upper()