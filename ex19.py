#define a function named cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#call the function with 2 parameters directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#assign a variable amount for cheese and crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#call the function with 2 variables as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#call the function with math as the parameters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#call the function using the variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#Study bit, write a function and run it 10 ways
def sandwhiches(bread,cheeseSlices,coldMeat):
    print "You have %d loafes of bread!" % bread
    print "You have %d cheese slices!" % cheeseSlices
    print "You have %d slices of Ham!" % coldMeat
    print "Man that's enough for a feast!"
    print "Picnic time!\n"

#numbers
sandwhiches(1,2,3)
sandwhiches(20,222,300)
#contain math
sandwhiches(1+3,2+2,3+1)
sandwhiches(1-3,2-2,3-1)
#predefined variables
breadLoafCount = 2
cheeseSlicesCount = 4
coldMeatCount = 6
sandwhiches(breadLoafCount,cheeseSlicesCount,coldMeatCount)


coldMeatCount = 6*6
sandwhiches(breadLoafCount,cheeseSlicesCount,coldMeatCount)

cheeseSlicesCount = 4*5
coldMeatCount = 6
sandwhiches(breadLoafCount,cheeseSlicesCount,coldMeatCount)

breadLoafCount = 2*5
cheeseSlicesCount = 4
coldMeatCount = 6
sandwhiches(breadLoafCount,cheeseSlicesCount,coldMeatCount)
#predefined variables + math
sandwhiches(breadLoafCount+1,cheeseSlicesCount+2,coldMeatCount+3)
sandwhiches(breadLoafCount+31,cheeseSlicesCount+22,coldMeatCount+38)
