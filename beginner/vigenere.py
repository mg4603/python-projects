try:
    from pyperclip import copy
except ImportError:
    pass

def main():
    display_intro()

    mode = get_mode()
    
    key = get_key()

    cipher = Vigenere(key)

    print('Enter message to {}.'.format(mode))
    message = input('> ')

    if mode == 'encrypt':
        translated = cipher.encrypt(message)
    elif mode == 'decrypt':
        translated = cipher.decrypt(message)
    
    print('{}ed message:'.format(mode.title()))
    print(translated)

    try:
        copy(translated)
        print('({}ed copied to clipboard.)'.format(mode))
    except NameError:
        pass

def display_intro():
    print('Vigenere Cipher')
    print()
    print('The Vigenere cipher is a poly-alphabetic substitution cipher')
    print('that was powerful enough to remain unbroken for centuries.')
    print()

def get_mode():
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    while True:
        response = input('> ').lower()
        if response == 'e':
            return 'encrypt'
        elif response == 'd':
            return 'decrypt'
        print('Please enter "e" or "d"')

def get_key():
    print('Please specify the key to use.')
    print('It can be a word or any combination of letters:')
    while True:
        response = input('> ').upper()
        if response.isalpha():
            return response
        print('The key must be a word or a combination of letters.')

class Vigenere:
    def __init__(s, key):
        assert key.isalpha(), \
            'Invalid key: key must be a word or a combination of letters'
        s.key = key
    
    def encrypt(s, message):
        return s.translate(message, 'encrypt')
    
    def decrypt(s, message):
        return s.translate(message, 'decrypt')

if __name__ == '__main__':
    main()