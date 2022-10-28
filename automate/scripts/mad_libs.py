from sys import argv, exit
from pyinputplus import inputStr

def parse_args():
    if len(argv) == 3:
        in_file = argv[1]
        out_file = argv[2]
        return {'in': in_file, 'out': out_file}
    elif len(argv) == 2:
        in_file = argv[1]
        return {'in', in_file}
    else:
        exit("Enter an option\n\t1. <input_file>\n\t2. <input_file> <output_file>\n")

def get_input(type):
    extra = ''
    if type[0] in ['a', 'e', 'i', 'o', 'u']:
        extra = 'n'
    prompt = "Enter a{} {}".format(extra, type)
    return inputStr(prompt)

def parse_text(text):
    text = list(text)
    for i, word in enumerate(text):
        if word.lower() == 'adjective':
            text[i] = get_input('adjective')
        elif word.lower() == 'noun':
            text[i] = get_input('noun')
        elif word.lower() == 'adverb':
            text[i] = get_input('adverb')
        elif word.lower() == 'verb':
            text[i] = get_input('verb')
        else:
            continue
    return ' '.join(text)
    
def main():
    pass