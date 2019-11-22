# heading = "Python: An Introduction, and Python: Advanced"
#            #header  Subheading
#            #partition takes an argument ----> returns a tuple collection
#            #breaks into 3 objects allows us to perform deconstruction
# header, _, subheader = heading.partition(': ')

# print(header)
# print(subheader)
#--------------------------------------------------------------

#SPLIT ALLOWS YOU TO BREAK UP EVERYTHING in a string and returns a LIST collection

#--------------------------------------------------------------

#tags = 'python,coding,programming,development'
# lists_of_tags = tags.split(',')

# print(lists_of_tags)
###converts into it's own stand alone string-it splits everything where there is a comma, converts into it's on elements

#---------------------------------------------------------------
# tags = 'python,coding,programming,development'
# lists_of_tags = tags.split()

# print(lists_of_tags)
###with no arguments it prints everything into an array in a list

#----------------------------------------------------------------

heading = "Python: An Introduction"

heading_list = heading.split(': ')

print(heading_list)

# above prints a list of elements
