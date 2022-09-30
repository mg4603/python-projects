def comma_code(spam):
    if(len(spam) == 0):
        return "List empty"
    
    if(len(spam) == 1):
        return spam[0]
    
    return "%s and %s" %(", ".join(spam[:-1]), spam[-1])

from random import randint
from tempfile import tempdir

def hundred_flips():
    return [randint(0,1) for i in range(100)]

def check_for_six_streak(row):
    num_of_streaks = 0
    streak_length = 1
    for i in range(1, len(row)):
        if(row[i] == row[i-1]):
            streak_length += 1
        else:
            streak_length = 1
        
        if(streak_length == 6):
            num_of_streaks += 1
            streak_length = 1
    return num_of_streaks

def coin_flip_streaks():
    total_num_of_streaks = 0
    for _ in range(10000):
        temp_row = hundred_flips()
        total_num_of_streaks += check_for_six_streak(temp_row)

    return total_num_of_streaks/ 10000 

print(coin_flip_streaks())

print(comma_code(['apples', 'bananas', 'tofu', 'cats']))

