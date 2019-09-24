# heading = "Python: An Introduction, and Python: Advanced"
#            #header  Subheading
#            #partition takes an argument ----> returns a tuple collection
#            #breaks into 3 objects allows us to perform deconstruction
# header, _, subheader = heading.partition(': ')

# print(header)
# print(subheader)
#-----------------------------------------------------------------------------------


#SPLIT ALLOWS YOU TO BREAK UP EVERYTHING in a string
# tags = 'python,coding,programming,development'

# lists_of_tags = tags.split(',')
# #converts into it's own stand alone string 
# print(lists_of_tags)
# 

# tags = 'python,coding,programming,development'

# lists_of_tags = tags.split()

# print(lists_of_tags)

heading = "Python: An Introduction"

heading_list = heading.split(': ')

print(heading_list)
