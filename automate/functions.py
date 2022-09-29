def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

