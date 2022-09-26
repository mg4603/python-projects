the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# We can similarly go through mixed lists 
# Note that %r has to be used as a format specifier since we con't know what is in it
for i in change:
    print("I got %r" % i)

# We can also build lists, fist start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to elements" % i)
    # append is a function that lists understand
    elements.append(i)

# elements = list(range(0, 6))

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)