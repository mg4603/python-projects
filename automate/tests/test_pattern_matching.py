from scripts.pattern_matching import findPhNumber, isPhoneNumber, q20, q21


def test_isPhoneNumber():
    assert isPhoneNumber('01234567891')
    assert isPhoneNumber('01234-567891')
    assert not isPhoneNumber('0123456789')
    assert not isPhoneNumber('0123-123121')

def test_findPhNumber():
    assert findPhNumber('My number is 01234-567891') == 'Phone number found: 01234-567891'
    assert findPhNumber('No phone number here') == 'No phone number found in text'

def test_q20():
    assert q20('42')
    assert q20('1,234')
    assert q20('6,368,745')
    assert not q20('12,34,567')
    assert not q20('1234')

def test_q21():
    assert q21('Haruto Watanabe')
    assert q21('Alice Watanabe')
    assert q21('RoboCop Watanabe')

    assert not q21('haruto Watanabe')
    assert not q21('Mr. Watanabe')
    assert not q21('Watanabe')
    assert not q21('Haruto watanabe')