def comma_code(spam):
    if(len(spam) == 0):
        return "List empty"
    
    if(len(spam) == 1):
        return spam[0]
    
    return "%s and %s" %(", ".join(spam[:-1]), spam[-1])

from random import randint

def hundred_flips():
    return [randint(0,1) for i in range(100)]

def check_for_six_streak(row):
    num_of_streaks = 0
    streak_length = 1
    for i in range(1, len(row)):
        if(row[i] == row(i-1)):
            streak_length += 1
        else:
            streak_length = 1
        
        if(streak_length == 6):
            num_of_streaks += 1
            streak_length = 1
    return num_of_streaks


print(comma_code(['apples', 'bananas', 'tofu', 'cats']))

