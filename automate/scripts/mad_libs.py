from pathlib import Path
import sys
import pyinputplus as pyip

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
    prompt = "Enter a{} {}".format(extra, type)
    return pyip.inputStr(prompt)

def parse_text(text):
    text = text.split()
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