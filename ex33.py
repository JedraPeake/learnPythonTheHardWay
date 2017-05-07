i = 0
numbers = []

def func(num, incr):
    for i in range(0,num,incr):
        print "At the top i is %d" % i
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


#while i < 6:
#    print "At the top i is %d" % i
#    numbers.append(i)
#
#    i = i + 1
#    print "Numbers now: ", numbers
#    print "At the bottom i is %d" % i
