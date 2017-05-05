# assign the string to x, with 10 replacing the formatting char
x = "There are %d types of people." % 10
# assign binary to binary
binary = "binary"
# assign don't to do_not
do_not = "don't"
# assign the string to y, with binary and do not replacing the respective formatting char
y = "Those who know %s and those who %s." % (binary, do_not)        #two strings in a string
#print x
print x
#print y
print y
# print the string with the whole var x replacing the formatting char
print "I said: %r." % x         # One string inside of a string
# print the string with with the whole var y replacing the formatting char
print "I also said: '%s'." % y          # One string inside of a string
#assign hilarious to false
hilarious = False
# assign the string to joke_evaluation, with an unevaluated formatting char
joke_evaluation = "Isn't that joke so funny?! %r"
#evaluate formatting char
print joke_evaluation % hilarious           # One string inside of a string
# Assign the string to w
w = "This is the left side of..."
# Assign the string to e
e = "a string with a right side."
#print w then e
print w + e         ## Concatenate two strings with + operator
