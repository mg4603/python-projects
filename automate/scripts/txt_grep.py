from pathlib import Path
import sys

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

