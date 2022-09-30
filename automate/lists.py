def comma_code(spam):
    if(len(spam) == 0):
        return "List empty"
    
    if(len(spam) == 1):
        return spam[0]
    
    return "%s and %s" %(", ".join(spam[:-1]), spam[-1])

from random import randint

def hundred_flips():
    return [randint(0,1) for i in range(100)]



print(comma_code(['apples', 'bananas', 'tofu', 'cats']))

