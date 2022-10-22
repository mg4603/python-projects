from scripts.extract_urls import url_extractor

def test_url_extractor():
    assert url_extractor('http://google.com') == 'http://google.com'
    assert url_extractor('https://accounts.google.com') == 'https://accounts.google.com'
    assert url_extractor('http://google.com https://accounts.google.com') \
        == 'http://google.com\nhttps://accounts.google.com'
    assert url_extractor('https://accounts.google.edu.uk') == 'https://accounts.google.edu.uk'
    