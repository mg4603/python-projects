from pathlib import Path
import sys
import pyinputplus as pyip
from re import IGNORECASE, compile, sub

def parse_args():
    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
        return {'in': in_file, 'out': out_file}
    elif len(sys.argv) == 2:
        in_file = sys.argv[1]
        return {'in': in_file}
    else:
        sys.exit("Enter an option\n\t1. <input_file>\n\t2. <input_file> <output_file>\n")

def get_input(type):
    extra = ''
    if type[0] in ['a', 'e', 'i', 'o', 'u']:
        extra = 'n'
    prompt = "Enter a{} {}: ".format(extra, type)
    return pyip.inputStr(prompt, blockRegexes=['[a-zA-Z0-9] [a-zA-Z0-9]'])

def parse_text(text):
    text = text.split()
    for i, word in enumerate(text):
        if 'adjective' in word.lower() :
            text[i] = sub('adjective', get_input('adjective'), word, flags=IGNORECASE)
        elif 'noun' in word.lower():
            text[i] = sub('noun', get_input('noun'), word, flags=IGNORECASE)
        elif 'adverb' in word.lower():
            text[i] = sub('adverb', get_input('adverb'), word, flags=IGNORECASE)
        elif 'verb' in word.lower():
            text[i] = sub('verb', get_input('verb'), word, flags=IGNORECASE)
        else:
            continue
    return ' '.join(text)
    
def main():
    args = parse_args()
    with Path(args['in']).open('r') as file:
        text = file.read()
    out_text = parse_text(text)
    if args.get('out', None):
        with Path(args['out']).open('w') as file:
            file.write(out_text)
    else:
        print(out_text)

if __name__ == "__main__":
    main()