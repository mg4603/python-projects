from random import randint


def num_input_validator(num, msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break
    
    return num

def is_prime(num: int) -> bool:
    if num <= 3:
        return num > 1

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True


def hint_gen(guess, num, hints):
    print("Here's a hint:")
    if hint == 8 or hint == 1 or hint == 3 or hint == 5 or hint == 7 or hint == 9:
        if guess < num:
            print("The number is larger than "+str(guess)+".")
        else:
            print("The number is smaller than "+str(guess)+".")
    elif hint == 2:
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    elif hint == 4:
        print(str(num * randint(1,4)) +" is a multiple of the number.")
    elif hint == 6:
        print(str(num * randint(5, 10))+ " is a multiple of the number.")
    elif hint == 10:
        if is_prime(num):
            print("The number is prime.")
        else:
            print("The number is composite.")

low,high,guess = 0,0,0
while True:
    hints = []
    low = num_input_validator(low, "Enter a number")
    high = num_input_validator(high, "Enter a number larger than "+str(low)+".")

    num = randint(low, high)
    score = 100

    while True:
        if score <= 0:
            print("You  lose!")
            break
        guess = num_input_validator(guess, "Enter a number between "+str(low)+" and "+str(high)+".")
    
        if guess == num:
            print("Congratulations! The number is "+str(guess)+". \n Your score is "+str(score)+".")
            break

        if guess != num:
            score -= 10
            print("Incorrect Guess! Try again.")
            hint = randint(1, 10)
            while hint in hints:
                hint = randint(1, 10)
            hints.append(hint)
            hint_gen(guess,num,hints)
    
    while True:
        try:
            choice = input("Do you want to play again?(Y/n)")
            if choice.lower() != 'y' and  choice.lower() != 'n':
                raise(ValueError)
            else:
                break
        except ValueError:
            print("Enter a valid input")
            continue
        else:
            break
    
    if choice.lower() == 'n':
        break
