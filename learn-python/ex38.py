ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

"""
Translates to:
    - split(ten_things, " ")
    - split ten_things using " " as delimiter
    - call split with ten_things and " "
"""
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    """
    Translates to:
        - pop(more_stuff)
        - pop last element of more_stuff
        - call pop with more_stuff
    """
    next_one = more_stuff.pop()
    print("Adding: %s" % next_one)
    """
    Translates to:
        - append(stuff, next_one)
        - append next_one to stuff
        - call append with stuff and next_one
    """
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: %s" % stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
"""
Translates to:
    - pop(stuff)
    - pop last element of stuff
    - call pop with stuff
"""
print(stuff.pop())
"""
Translates to:
    - join(stuff, " ")
    - join stuff with " " between them
    - call join with stuff and " "
"""
print(" ".join(stuff))
"""
Translates to:
    - join(stuff[3:5], "#")
    - join 3rd and 4th element of stuff with "#" between them
    - call join with stuff[3:5] and "#"
"""
print("#".join(stuff[3:5]))