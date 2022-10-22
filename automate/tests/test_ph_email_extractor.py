from scripts.ph_email_extractor import ph_number_extractor, email_extractor, extractor

def test_ph_number_extractor():
    assert ph_number_extractor('2242081524') == ['22-4208-1524']
    assert ph_number_extractor('42081524') == ['4208-1524']
    assert ph_number_extractor('22-4208-1524') == ['22-4208-1524']
    