from re import compile, VERBOSE
from tokenize import group

def extract_date(text):
    date_regex = compile(
        r'''
        (0[1-9]|[12][0-9]|[3][01])  # day
        /                           # separator
        (0[1-9]|1[0-2])             # month
        /                           # separator
        ([12][0-9]{3})              # year
        ''',
        VERBOSE
    )
    dates = date_regex.findall(text)
    return [list(date_group)  for date_group in dates if date_group]

def check_30_days(date):
    days_30_regex = compile(
        r'(0[1-9]|[12][0-9]|[3][0])'
    )
    return days_30_regex.search(date)

def check_31_days(date):
    days_31_regex = compile(
        r'(0[1-9]|[12][0-9]|[3][01])'
    )
    return days_31_regex.search(date)

def check_leap_feb(date):
    leap_feb_regex = compile(
        r'(0[1-9]|[12][0-9])'
    )
    return leap_feb_regex.search(date)

def check_non_leap_feb(date):
    non_leap_feb_regex = compile(
        r'(0[1-9]|[1][0-9]|2[0-8])'
    )
    return non_leap_feb_regex.search(date)


def is_valid_date(date):
    days_31 = ['01', '03', '05', '07', '08', '10', '12']
    
    if date:
        if date[1] == '02':
            year = int(date[2])
            if year % 4 == 0:
                if year % 400 == 0:
                    return check_leap_feb(date[0])
                elif year % 100 == 0:
                    return check_non_leap_feb(date[0])
                else:
                    return check_leap_feb(date[0])
            else:
                return check_non_leap_feb(date[0])
        elif date[1] not in days_31:
            return check_30_days(date[0])
        else:
            return check_31_days(date[0])
    else:
        return False