from scripts.date_detection import (
    check_30_days, check_31_days, check_leap_feb, extract_date, 
    is_valid_date, check_non_leap_feb
) 

def test_date_detection():
    assert extract_date(
        '''
        12/12/2020
        31/04/2021
        31/02/2020
        '''
    ) \
        == [
            ['12', '12', '2020'],
            ['31', '04', '2021'],
            ['31', '02', '2020']
        ]
    assert not extract_date(
        """ 
        51/01/2020
        45/01/2020
        25/91/2020
        15/15/2020
        15/12/3000
        """
    )
def test_check_30_days():
    assert check_30_days('12')
    assert check_30_days('30')
    assert not check_30_days('00')
    assert not check_30_days('51')

def test_check_31_days():
    assert check_31_days('12')
    assert check_31_days('31')
    assert not check_31_days('32')
    assert not check_31_days('00')
    assert not check_31_days('1')
    assert not check_31_days('51')

def test_check_leap_feb():
    assert check_leap_feb('12')
    assert check_leap_feb('29')
    assert not check_leap_feb('30')
    assert not check_leap_feb('00')
    assert not check_leap_feb('1')
    assert not check_leap_feb('51')
