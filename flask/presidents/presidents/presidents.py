class OrdError(Exception):
    pass

def isInt(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False

