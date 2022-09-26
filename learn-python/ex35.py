from multiprocessing.sharedctypes import Value
from sys import exit

prompt = "> "

def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


