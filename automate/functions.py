def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def collatz_sequence():

    num = input("Enter an integer:\n")    
    while(True):
        if(isNum(num)):
            num = int(num)
            break
        else:
            print("Enter a number")
            num = input()
    
    
    while(num != 1):
        if(num % 2 == 0):
            num //= 2
        else:
            num = 3 * num + 1
        print(num)
