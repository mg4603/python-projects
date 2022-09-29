# Q9 flow control practice question
def Q9(spam):
    if(spam == 1):
        print("Hello")
    elif(spam == 2):
        print("Howdy")
    else:
        print("Greetings")

def Q13():
    print("-"*10)
    print("For loop:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n%s" %("-"*10))
    print("While Loop:")
    i = 1
    while(i < 11):
        print(i, end=" ")
        i+=1
    
    print()

Q13()