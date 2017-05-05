print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#study drill bit
# raw_input(): Read a string from standard input.
#input(): Read a value from standard input.

#additinal form
print "Enter a soccer players name: ",
name = raw_input()
print "What is %s's postion?" % name,
age = raw_input()
print "What is %s's nationaity?" % name,
height = raw_input()
print "What is %s's club name?" % name,
weight = raw_input()
print "How many goals has %s scored?" % name,
goals = raw_input()

print "So, you chose %r,who plays %r, for %r and %r, scoring %r goals." % (
    name, age, height, weight, goals)
