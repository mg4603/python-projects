from scripts.pattern_matching import isPhoneNumber


def test_isPhoneNumber():
    assert isPhoneNumber('01234567891')
    assert isPhoneNumber('01234-567891')
    assert not isPhoneNumber('0123456789')
    assert not isPhoneNumber('0123-123121')