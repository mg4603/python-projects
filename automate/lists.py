def comma_code(spam):
    if(len(spam) == 0):
        return "List empty"
    
    if(len(spam) == 1):
        return spam[0]
    
    return "%s and %s" %(", ".join(spam[:-1]), spam[-1])

print(comma_code(['apples', 'bananas', 'tofu', 'cats']))
