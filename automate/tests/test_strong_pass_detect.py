from scripts.strong_pass_detect import (
    check_length, check_upper
) 

def test_check_length():
    assert check_length('asdfghjl')
    assert check_length('asd ghjk')
    assert check_length('asd@1 jk')
    assert not check_length('asdf')
    assert not check_length('asdf123')

def test_check_upper():
    assert check_upper('Aasdf')
    assert check_upper('asfAasdf')
    assert check_upper('  A  ')
    assert not check_upper('asfd')
    assert not check_upper('1234')