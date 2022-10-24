from scripts.strip import strip

def test_strip():
    assert strip(' asfd') == 'asfd'
    assert strip('asdf', 'a') == 'sdf'
    assert strip('asdf', 'af') == 'sd'