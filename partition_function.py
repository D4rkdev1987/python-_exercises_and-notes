
heading = "Python: An Introduction"
           #header     Subheading          
header, _, subheader = heading.partition(': ')

print(header, subheader)

# first create te variable heading with a string Python heading then a colon with An introduction
# next 3 variables in a row starting with header then an underscore and then a subheader
# then assign them to the heading.partition which takes in argument and returns what ever is in it
# it seperates into 3 elements 1st python 2nd is the colon and the 3rd An Introduction
##what ever is put into the _ it's a throw away value-in this case its the colon :  
##partition takes an argument ----> returns a tuple collection
##breaks string into 3 objects allows us to perform  variable deconstruction