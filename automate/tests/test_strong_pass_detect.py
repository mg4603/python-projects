from scripts.strong_pass_detect import check_length

def test_check_length():
    assert check_length('asdfghjl')
    assert check_length('asd ghjk')
    assert check_length('asd@1 jk')
    assert not check_length('asdf')
    assert not check_length('asdf123')