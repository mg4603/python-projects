from pathlib import Path
from scripts.txt_grep import check_line, get_filenames, read_file, parse_args
from re import compile

def test_get_filenames():
    assert get_filenames(Path('./tests')) == [Path('tests/text.txt')]

def test_read_file():
    assert read_file(Path('./tests/text.txt')) == ['text grep file: some random content\n']

def test_check_line():
    regex = compile(':')
    assert check_line(regex, 'text grep file: some random content\n') == 'text grep file: some random content\n'
    assert check_line(regex, 'text grep file some random content\n') == None

def test_parse_args(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('sys.argv', ['../scripts/txt_grep.py', './tests/', ':'])
        args_dict = parse_args()
    assert args_dict == {'path': './tests/', 'regex': ':'}