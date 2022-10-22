from scripts.ph_email_extractor import ph_number_extractor, email_extractor, extractor

def test_ph_number_extractor():
    assert ph_number_extractor('2242081524') == ['22-4208-1524']
    assert ph_number_extractor('42081524') == ['4208-1524']
    assert ph_number_extractor('22-4208-1524') == ['22-4208-1524']

def test_email_extractor():
    assert email_extractor(('lol@lol.lol.edu')) == ['lol@lol.lol.edu']
    assert email_extractor('asf lol.lol@lol.gov.us asdf') == ['lol.lol@lol.gov.us']

def test_extractor():
    assert extractor('4208-1524') == \
        'Phone Numbers: \n\t4208-1524\nEmails: \n\t'
    assert extractor('4208-1524 lol.lol@lol.gov.us') == \
        'Phone Numbers: \n\t4208-1524\nEmails: \n\tlol.lol@lol.gov.us'