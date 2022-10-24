from scripts.strong_pass_detect import (
    check_chars, check_length, check_lower, check_upper
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

def test_check_lower():
    assert check_lower('aASDF')
    assert check_lower('ASfASDF')
    assert check_lower('  a  ')
    assert not check_lower('ASFD')
    assert not check_lower('1234')

def test_check_chars():
    assert check_chars('aAsdf')
    assert check_chars('ASDFa ')
    assert check_chars('1234aA')
    assert not check_chars('123456')
    assert not check_chars('1234a')
    assert not check_chars('1234A')