from scripts.date_detection import check_30_days, extract_date, is_valid_date

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
