from csv import DictReader

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

def convert_to_dict(path_to_csv):
    with open(path_to_csv) as f:
        result = [{k: v for k,v in row.items()}
                 for row in DictReader(f, skipinitialspace=True)]
    return result


def presidency_president_pairs_list(presidents_list):
    pairs_list = []
    for president in presidents_list:
        pairs_list.append((president["Presidency"], president["President"]))
    return pairs_list