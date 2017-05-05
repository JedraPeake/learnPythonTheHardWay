tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#code to try
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#more complex bit
print "%s" % "She said \"hey\""     #qoute in a qoute
months = "Jan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug"
print months
