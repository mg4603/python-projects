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

if __name__ == '__main__':
    main()