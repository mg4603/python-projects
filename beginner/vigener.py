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

if __name__ == '__main__':
    main()