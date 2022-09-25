from sys import argv

script, filename = argv

print((f"We are going to erase the file {filename}"))
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")