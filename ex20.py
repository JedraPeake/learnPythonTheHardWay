#import argv variables from the system input
from sys import argv
#unpack argv
script, input_file = argv
#define print all function
def print_all(f):
    #print the file contents
    print f.read()
#define rewind function
def rewind(f):
    #make the file reader return to the byte of the file
    f.seek(0)
#define print a line function
def print_a_line(line_count, f):
    #print a line number, and eveyhting on the line
    print line_count, f.readline()
#open a file
current_file = open(input_file)
#print text
print "First let's print the whole file:\n"
#call the print all function
print_all(current_file)
#print text
print "Now let's rewind, kind of like a tape."
#call the rewind function
rewind(current_file)
#print text
print "Let's print three lines:"
#set a current line
current_line = 1
#call the print_a_line function
print_a_line(current_line, current_file)
#set a current line
current_line += 1
#call the print_a_line function
print_a_line(current_line, current_file)
#set a current line
current_line += 1
#call the print_a_line function
print_a_line(current_line, current_file)
