people = 30
cars = 30
buses = 30

if(cars > people):
    print("We should take the cars.")
elif(cars < people):
    print("We shouldn't take the cars.")
else:
    print("We can't decide.")


if(buses > cars):
    print("That's too many buses.")
elif(buses < cars):
    print("Maybe we could take buses.")
else:
    print("We still can't decide.")

if(people > buses):
    print("Alright let's just take the buses.")
else:
    print("Fine, let's stay home then.")