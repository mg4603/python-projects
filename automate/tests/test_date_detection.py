from scripts.date_detection import extract_date

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