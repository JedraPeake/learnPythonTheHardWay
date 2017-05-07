def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# switch the order of multiply and divide
what = add(age, subtract(height, divide(weight, multiply(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# A new puzzle.
print "Here is a new puzzle."

# write a simple formula and use the function again
up = 5
down = 10
tall = 15
what2 = divide(multiply(tall, add(up, down)), 2)

print "That become: ", what2
