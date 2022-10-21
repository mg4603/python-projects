def isPhoneNumber(string):
    if len(string) != 11 and len(string) != 12:
        return False

    for i in range(0, 6):
        if not string[i].isdecimal():
            return False
    
    if len(string) == 12:
        if string[6] != ' ' and string[6] != '-':
            return False
        for i in range(7, 12):
            if not string[i].isdecimal():
                return False
    else:
        for i in range(6, 11):
            if not string[i].isdecimal():
                return False
    
    return True

print(isPhoneNumber('012345-67891'))