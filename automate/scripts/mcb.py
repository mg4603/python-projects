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

def parse_args():
    pass

def load_shelf():
    with shl_open('mcb') as mcb_shelf:
        pass

def save_shelf(selfValues):
    pass

