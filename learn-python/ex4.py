cars = 100
space_in_a_car = 4.0
drivers = 3
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_a_car * cars_driven
average_passenger_per_car =  passengers / cars_driven

print("There are %s cars available." % cars)
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passenger_per_car} in each car.")
