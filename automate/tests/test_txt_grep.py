from pathlib import Path
from scripts.txt_grep import get_filenames, read_file

def test_get_filenames():
    assert get_filenames(Path('./tests')) == [Path('tests/text.txt')]

def test_read_file():
    assert read_file(Path('./tests/text.txt')) == ['text grep file: some random content\n']