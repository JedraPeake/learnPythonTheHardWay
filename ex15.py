#imports argv from user input when running script
from sys import argv
# unpacks argv, assiging ex15.py to script and ex15_sample.txt to filename
script, filename = argv
#opens filename
txt = open(filename)
#prints heres your file with the filename on the end
print "Here's your file %r:" % filename
#prints the file
print txt.read()
#prints text
print "Type the filename again:"
#asks for input using prompt
file_again = raw_input("> ")
#opens file again
txt_again = open(file_again)
#prints txt_again
print txt_again.read()

# close the file
txt.close()
txt_again.close()
