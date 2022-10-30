from pathlib import Path
from scripts.rename_dates import contains_american_date, generate_european_date, get_filenames

def test_contain_american_date():
    assert contains_american_date('12-2-2022asdf.txt')
    assert contains_american_date('asdf7-12-2022pohasdf.txt')
    assert not contains_american_date('asdf13-13-2022.txt')
    assert not contains_american_date('fasd09-33-2022.txt')

def test_get_filenames():
    assert get_filenames(Path('../scripts/')) == list(Path('../scripts/').rglob('*'))

def test_generate_european_date():
    assert generate_european_date('asdf12-2-2022asdf.txt') == 'asdf2-12-2022asdf.txt'
    assert generate_european_date('12-2-2022asdf.txt') == '2-12-2022asdf.txt'
    assert generate_european_date('asdf2-12-2022asdf.txt') == 'asdf12-2-2022asdf.txt'
    assert generate_european_date('5-31-2024.txt') == '31-5-2024.txt'