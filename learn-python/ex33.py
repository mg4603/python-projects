def fn(end, step=1):
    i = 0
    numbers = []

    while(i < end):
        print("At the top i is %d" % i)
        
        numbers.append(i)
        i += step
    
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for number in numbers:
        print(number)

fn(6)