# helper functions
import re

#validation base function  
def validation(input_msg, condition):
    while True:
        try:
            user_input = input(msg)
            if condition(user_input):
                raise(ValueError)
        except ValueError:
            print("Enter a valid input")
            continue
        else:
            break
    return user_input


# condition of accepting y/n input
def condition_y_n(user_input) -> bool:
    if user_input.lower() != 'y' and user_input.lower() != 'n':
        return True
    return False

# function to accept input of y or n
def validated_y_n(msg):
    return validation(msg, condition_y_n)


# condition for numeric input
def condition_num(user_input) -> bool:
    return not user_input.isnumeric()

# function to accept a number
def validated_number(msg):
    return validation(msg, condition_num)


# condition for a alphabetic input
def condition_alpha(user_input) -> bool:
    return not user_input.isalpha()

# function to accept a letter as input
def validated_alpha(msg):
    return validation(msg, condition_num)


# condition for accepting a name as input
def condition_name(user_input) -> bool:
    return not re.search("[A-Za-z][a-z'-]+", user_input)

# function to accept a name
def validated_name(msg):
    return validation(msg, condition_name)

#condition for accepting an email
def condition_email(user_input) -> bool:
    return not re.search("([a-z1-9]+@[a-z]+(.[a-z]+)+)", user_input)

# function to accept an email
def validated_email(msg):
    return validation(msg, email)


