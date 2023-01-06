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