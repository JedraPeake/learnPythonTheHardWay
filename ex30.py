#assign values to variables
people = 30
cars = 40
trucks = 15

#if we have more cars than poeple print we should take cars
if cars > people:
    print "We should take the cars."
#else if we have more poeple than cars print we should not take cars
elif cars < people:
    print "We should not take the cars."
#if cars =poeple print we cant decide
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

#study drills
#elif is like an extension of if an if were it can enter a different branch, it always enters else
