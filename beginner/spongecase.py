from random import randint
try:
    from pyperclip import copy
except ImportError:
    pass


def english_to_spongecase(msg):
    use_upper = False
    sponge_text = ''
    for char in msg:
        if not char.isalpha():
            sponge_text += char
        
        if use_upper:
            sponge_text += char.upper()
        else:
            sponge_text += char.lower()

        if randint(1, 100) <= 90:
            use_upper = not use_upper
    
    return sponge_text

if __name__ == '__main__':
    main()