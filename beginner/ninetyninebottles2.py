from sys import exit
from random import randint
from time import sleep

class NinetyNineBottles2:
    def __init__(s, bottles = 99):
        s.bottles = bottles
        s.lines = [
            ' bottles of milk on the wall,',
            ' bottles of milk,',
            'Take one down, pass it around,',
            ' bottles of milk on the wall!'
        ]
    
    def display_intro(s):
        print('nNin Ty-nnIiNe boTtlles')
        print()
        print('(Press CTRL-C to quit.)')
        sleep(2)
    
    def effect_one(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        char_index = randint(0, len(line) - 1)
        line[char_index] = ' '
        s.lines[line_num] = ''.join(line)
    
    def effect_two(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        char_index = randint(0, len(line) - 1)
        char = line[char_index]
        if char.islower():
            line[char_index] = char.upper()
        elif char.isupper():
            line[char_index] = char.lower()
        s.lines[line_num] = ''.join(line)
    
    def effect_three(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        char_index = randint(0, len(line) - 2)
        line[char_index], line[char_index + 1] = \
            line[char_index + 1], line[char_index]
        s.lines[line_num] = ''.join(line)
    
    def effect_four(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        char_index = randint(0, len(line) - 1)
        line.insert(char_index, line[char_index])
        s.lines[line_num] = ''.join(line)
    
    def effect_five(s):
        line_num = randint(0, 3)
        line = s.lines[line_num].split(' ')
        word_index = randint(0, len(line) - 1)
        if line[word_index].isupper():
            line[word_index].lower()
        else:
            line[word_index].upper()
        s.lines[line_num] = ' '.join(line)

if __name__ == '__main__':
    obj = NinetyNineBottles2()
    obj.display_intro()
    try:
        obj.main()
    except KeyboardInterrupt:
        exit()