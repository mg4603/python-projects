try:
    from pyperclip import copy
except ImportError:
    pass

class Rot13:
    UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(s):
        pass

    def translate(s, message):
        translated = ''
        for char in message:
            if char.isupper():
                translated += s.UPPER_LETTERS[(ord(char) - 65 - 13) % 26]
            elif char.islower():
                translated += s.LOWER_LETTERS[(ord(char) - 97 - 13) % 26]
            else:
                translated += char
        return translated
    
    def display_intro(s):
        print('ROT13 Cipher')
        print()

def main():
    cipher = Rot13()
    cipher.display_intro()
    while True:
        print('Enter a message to encrypt/decrypt (or CTRL-C to quit.):')
        message = input('> ')
        translated_msg = cipher.translate(message)
        print('The translated message is:')
        print(translated_msg)
        print()
        try:
            copy(translated_msg)
            print('(Copied to clipboard.)')
        except ValueError:
            pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()