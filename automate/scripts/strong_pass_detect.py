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