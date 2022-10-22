from re import VERBOSE, compile
from pyperclip import copy, paste

def url_extractor(text):
    url_regex = compile(
        r'''
        (https?://)
        ([a-zA-Z.1-9]+)
        (\.[a-zA-Z]{2,3})
        (\.[a-zA-Z]{2})?
        ''',
        VERBOSE
    )

    return '\n'.join([''.join([group for group in url_groups if group]) for url_groups in  url_regex.findall(text)])

if __name__ == "__main__":
    text = paste()
    urls = url_extractor(text)
    copy(urls)