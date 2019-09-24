heading = "Python: An Introduction"
           #header  Subheading
           #partition takes an argument ----> returns a tuple collection
           #breaks into 3 objects allows us to perform deconstruction
header, _, subheader = heading.partition(': ')

print(header, subheader)
