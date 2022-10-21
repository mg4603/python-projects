from scripts.pattern_matching import findPhNumber, isPhoneNumber


def test_isPhoneNumber():
    assert isPhoneNumber('01234567891')
    assert isPhoneNumber('01234-567891')
    assert not isPhoneNumber('0123456789')
    assert not isPhoneNumber('0123-123121')

def test_findPhNumber():
    assert findPhNumber('My number is 01234-567891') == 'Phone number found: 01234-567891'
    assert findPhNumber('No phone number here') == 'No phone number found in text'