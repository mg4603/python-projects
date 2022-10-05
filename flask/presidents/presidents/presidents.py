class OrdError(Exception):
    pass

def isInt(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False

def make_ordinal(num):
    """
    Convert an integer into its ordinal representation
    """
    if(isInt(num)):
        num = int(num)
    
    if 11 <= (num%100) <= 13:
        return str(num)+"th"
    else:
        return str(num)+["th", "st", "nd", "rd", "th"][min(num%10, 4)]
