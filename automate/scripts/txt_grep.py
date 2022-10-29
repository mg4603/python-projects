from pathlib import Path
import sys
from re import compile

def get_filenames(path):
    return [filename for filename in path.rglob('*.txt')]

def read_file(path):
    with path.open('r') as file:
        lines = file.readlines()
    return lines

def check_line(regex, line):
    if regex.search(line):
        return line
    return None

def parse_args():
    if len(sys.argv) == 3:
        return {'path': sys.argv[1], 'regex': sys.argv[2]}    
    exit(
        'usage: python3 txt_grep.py [path] [regex]\npath: path in which to check for .txt files'
    )

def main():
    args = parse_args()
    if Path(args['path']).exists():
        dir_path = Path(sys.argv[1])

    filenames = get_filenames(dir_path)
    result = []
    for filename in filenames:
        lines = read_file(Path(filename))
        for line in lines:
            regex = compile(
                args['regex']
            )
            result.append(check_line(regex, line))
