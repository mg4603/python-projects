from sys import exit
try:
    from pyperclip import copy
except ImportError:
    pass

class PigLatin:
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    def __init__(s):
        pass

    def english_to_pig_latin(s, message):
        pig_latin = ''
        for word in message.split():
            prefix_non_letters = ''
            suffix_non_letters = ''
            prefix_consonants = ''

            while len(word) > 0 and not word[0].isalpha():
                prefix_non_letters += word[0]
                word = word[1:]
            
            if len(word) == 0:
                pig_latin += prefix_non_letters + ' '
                continue

            while not word[-1].isalpha():
                suffix_non_letters += word[-1]
                word = word[:-1]
            
            while len(word) > 0 and not word[0] in s.VOWELS:
                prefix_consonants += word[0]
                word = word[1:]
            
            if prefix_consonants != '':
                word += prefix_consonants + 'ay'
            else:
                word += 'yay'

            pig_latin += prefix_non_letters + word + suffix_non_letters + ' '
        return pig_latin
    
def main():
    converter = PigLatin()
    try:
        while True:
            print('Enter you message (or Press CTRL-C to quit.)')
            message = input('> ')
            pig_latin = converter.english_to_pig_latin(message)
            print(pig_latin)
            copy(pig_latin)
    except NameError:
        pass
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()