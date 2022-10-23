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
