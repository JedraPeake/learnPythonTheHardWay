# we have 100 cars, with space for 4 passangers, and only 30 drivers, with 90 passangers.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#cars_not_driven is total cars - drivers(100-70), and cars driven = drivers
cars_not_driven = cars - drivers
cars_driven = drivers
#carpool capacity is the total cars driven multiplied by the space in the cars
carpool_capacity = cars_driven * space_in_a_car
#average capacity is passangers divided by cars driven.
average_passengers_per_car = passengers / cars_driven

# prints text with a variable
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#explain the error
#carpool_capacity is defined not car_pool_capacity
