from pathlib import Path

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

