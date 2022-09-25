# Comments are used to describe what each line does

# Import argv from sys module
from sys import argv

# Unpack argv into script and file_name variables
script, file_name = argv

# Call built-in function open from io module
txt = open(file_name)

print(f"Here's your file {file_name}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())