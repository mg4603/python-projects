from pathlib import Path

def get_filenames(path):
    return [filename for filename in path.rglob('*.txt')]