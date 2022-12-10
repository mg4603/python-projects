class FactorFinder:
    def __init__(self):
        pass
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('------------------------Factor Finder------------------------')
        print('-------------------------------------------------------------')
        print()

def is_int(num):
    try:
        int(num)
        if num % 1 != 0:
            return False
        return True
    except:
        return False

def handle_inputs():
    pass