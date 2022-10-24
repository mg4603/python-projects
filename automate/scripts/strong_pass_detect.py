"""
Criteria:
    - eight characters long
    - contains both upper case and lowercase characters
    - has at least one digit
"""
from re import compile, DOTALL

def check_length(password):
    length_regex = compile(
        r'.{8,}',
        DOTALL
    )
    return length_regex.search(password)

def check_upper(password):
    upper_case_regex = compile(
        r'[A-Z]'
    )
    return upper_case_regex.search(password)

def check_lower(password):
    lower_case_regex = compile(
        r'[a-z]'
    )
    return lower_case_regex.search(password)

def check_digit(password):
    digit_regex = compile(
        r'[0-9]'
    )
    return digit_regex.search(password)

def check_chars(password):
    return check_lower(password) and check_upper(password)

def check_password(password):
    return check_length(password) and check_chars(password) and check_digit(password) 