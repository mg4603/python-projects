from re import compile, IGNORECASE

def isPhoneNumber(string):
    if len(string) != 11 and len(string) != 12:
        return False

    for i in range(0, 5):
        if not string[i].isdecimal():
            return False
    
    if len(string) == 12:
        if string[5] != ' ' and string[5] != '-':
            return False
        for i in range(6, 12):
            if not string[i].isdecimal():
                return False
    else:
        for i in range(5, 11):
            if not string[i].isdecimal():
                return False
    
    return True

def findPhNumber(text):
    phoneNumberRegex = compile(r'\d{5}(-?)\d{6}')
    number = phoneNumberRegex.search(text)
    if number is not None:
        return 'Phone number found: ' + number.group()
    return "No phone number found in text"

def q20(number_string):
    number_string_regex = compile(r'^(\d{1,3}(,\d{3})*)$')
    return number_string_regex.search(number_string)

def q21(name_string):
    name_regex = compile(r'[A-Z][a-zA-Z]* Watanabe')
    return name_regex.search(name_string)

def q22(text):
    q22_regex = compile(
        r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.',
        IGNORECASE
    )
    return q22_regex.search(text)