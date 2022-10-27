"""
1. The command line argument for the keyword is checked.
2. If the argument is save, then the clipboard contents are saved to
the keyword.
3. If the argument is list, then all the keywords are copied to the clipboard.
4. Otherwise, the text for the keyword is copied to the clipboard.
This means the code will need to do the following:
1. Read the command line arguments from sys.argv.
2. Read and write to the clipboard.
3. Save and load to a shelf file.
"""
from shelve import open as shl_open
from pyperclip import copy, paste
from sys import argv, exit

def main():
    if len(argv) == 3:
        if argv[1].lower() == 'save':
            pass
    elif len(argv) == 2:
        if argv[1].lower() == 'list':
            pass
        else:
            pass
    else:
        exit('Enter an option:\n\t1. save <keyword> : to save current \
        clipboard under <keyword>\n\t2. list : to copy all available keywords\
        to the clipboard\n\t3.<keyword> : to copy associated text from clipboard')


def load_shelf():
    shelf_dict = {}
    with shl_open('mcb') as mcb_shelf:
        shelf_dict = dict(mcb_shelf)
    return shelf_dict

def save_shelf(key, value):
    with shl_open('mcb') as mcb_shelf:
        mcb_shelf[key] = value

