from sys import exit
from random import randint
from time import sleep

class NinetyNineBottles2:
    LINE_PAUSE = 1.5
    SPEED = .01
    def __init__(s, bottles = 99):
        s.bottles = bottles
        s.lines = [
            ' bottles of milk on the wall,',
            ' bottles of milk,',
            'Take one down, pass it around,',
            ' bottles of milk on the wall!'
        ]
        s.upward_count = 0
    
    def display_intro(s):
        print('nNin Ty-nnIiNe boTtlles')
        print()
        print('(Press CTRL-C to quit.)')
        sleep(2)
    
    def effect_one(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        while True:
            char_index = randint(0, len(line) - 1)
            if line[char_index] != ' ':
                break

        line[char_index] = ' '
        s.lines[line_num] = ''.join(line)
    
    def effect_two(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        while True:
            char_index = randint(0, len(line) - 1)
            if line[char_index].isalpha():
                break

        char = line[char_index]
        if char.islower():
            line[char_index] = char.upper()
        elif char.isupper():
            line[char_index] = char.lower()
        s.lines[line_num] = ''.join(line)
    
    def effect_three(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        while True:
            char_index = randint(0, len(line) - 2)
            if line[char_index + 1] != ' ' and\
                    line[char_index] != line[char_index + 1] and\
                    line[char_index].isalpha():
                break

        line[char_index], line[char_index + 1] = \
            line[char_index + 1], line[char_index]
        s.lines[line_num] = ''.join(line)
    
    def effect_four(s):
        line_num = randint(0, 3)
        line = list(s.lines[line_num])
        while True:
            char_index = randint(0, len(line) - 1)
            if line[char_index] != ' ':
                break

        line.insert(char_index, line[char_index])
        s.lines[line_num] = ''.join(line)
    
    def effect_five(s):
        line_num = randint(0, 3)
        if s.lines[line_num][0] == ' ':
            add_space = True
        else:
            add_space = False
        line = s.lines[line_num].strip().split(' ')
        word_index = randint(0, len(line) - 1)
        if line[word_index].isupper():
            line[word_index] = line[word_index].lower()
        else:
            line[word_index] = line[word_index].upper()
        if add_space:
            s.lines[line_num] = ' ' + ' '.join(line)
        else:
            s.lines[line_num] = ' '.join(line)

    def effect_six(s):
        line_num = randint(0, 3)
        if s.lines[line_num][0] == ' ':
            add_space = True
        else:
            add_space = False
        line = s.lines[line_num].strip().split(' ')
        while True:
            word_index = randint(0, len(line) - 2)
            if line[word_index] != line[word_index + 1]:
                break
        line[word_index], line[word_index + 1] = \
            line[word_index + 1], line[word_index]
        if add_space:
            s.lines[line_num] = ' ' + ' '.join(line)
        else:
            s.lines[line_num] = ' '.join(line)
    
    def effect_seven(s):
        s.upward_count = randint(1, 3)
    
    def slow_print(s, text, pause_amt=0.1):
        for char in text:
            print(char, flush=True, end='')
            sleep(pause_amt)
        print()
    
    def main(s):
        while s.bottles > 0:
            s.slow_print(str(s.bottles) + s.lines[0], s.SPEED)
            sleep(s.LINE_PAUSE)
            s.slow_print(str(s.bottles) + s.lines[1], s.SPEED)
            sleep(s.LINE_PAUSE)
            s.slow_print(s.lines[2], s.SPEED)
            sleep(s.LINE_PAUSE)
            if s.upward_count > 0:
                s.bottles += 1
                s.upward_count -= 1
            else:
                s.bottles -= 1
            if s.bottles == 0:
                s.slow_print('No more' + s.lines[3], s.SPEED)
            else:
                s.slow_print(str(s.bottles) + s.lines[3], s.SPEED)
            sleep(s.LINE_PAUSE)
            print()

            effect = randint(1, 7)
            print(effect)
            if effect == 1:
                s.effect_one()
            elif effect == 2:
                s.effect_two()
            elif effect == 3:
                s.effect_three()
            elif effect == 4:
                s.effect_four()
            elif effect == 5:
                s.effect_five()
            elif effect == 6:
                s.effect_six()
            elif effect == 7:
                s.effect_seven()

if __name__ == '__main__':
    obj = NinetyNineBottles2(99)
    obj.display_intro()
    try:
        obj.main()
    except KeyboardInterrupt:
        exit()