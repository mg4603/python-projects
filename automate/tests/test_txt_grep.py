from pathlib import Path
from scripts.txt_grep import get_filenames

def test_get_filenames():
    assert get_filenames(Path('./tests')) == [Path('tests/text.txt')]