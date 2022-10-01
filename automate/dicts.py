from ast import excepthandler
import re
from sys import exit

def invalid_board(reason):
    print(reason)
    exit(0)

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def keyExists(dictionary, key):
    try:
        dictionary[key]
        return True
    except KeyError:
        return False