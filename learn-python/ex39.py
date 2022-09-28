states = {
    "Oregon"    :   "OR",
    "Florida"   :   "FL",
    "California":   "CA",
    "New York"  :   "NY",
    "Michigan"  :   "MI"
}

cities = {
    "CA"    : "San Francisco",
    "MI"    : "Detroit",
    "FL"    : "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print_delimiter = "-"*10

print(print_delimiter)
print("NY state has: %s" % cities["NY"])
print("OR state has: %s" % cities["OR"])

print(print_delimiter)
print("Michigan's abbreviation is: %s" % states["Michigan"])
print("Florida's abbreviation is: %s" % states["Florida"])

print(print_delimiter)
print("Michigan has: %s" % cities[states["Michigan"]])
print("Florida has: %s" % cities[states["Florida"]])

print(print_delimiter)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print(print_delimiter)
for abbrev, city in cities.items():
    print("%s has the cities %s" % (abbrev, city))

print(print_delimiter)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print(print_delimiter)
# Safely get item from dictionary that might not be there
state = states.get("Texas", None)

if(not state):
    print("Sorry, no Texas")

# set default value to be returned if dictionary doesn't have item
city = cities.get("TX", "Does not exist")
print("The city for the state 'TX' is: %s" % city)