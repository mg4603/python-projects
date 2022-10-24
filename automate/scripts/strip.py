from re import compile

def strip(string, characters=' '):
    if characters == ' ':
        regex_string = '[^ ]'.format()
    else:
        regex_string = '[^{}]'.format(''.join(characters.split()))
    strip_regex = compile(
        regex_string
    )
    return ''.join(strip_regex.findall(string))
