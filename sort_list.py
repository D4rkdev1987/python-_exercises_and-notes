# REMEMBER Lists in python are muteable 

tags = ['python', 'development', 'tutroials', 'code'] #list of tags here
print(tags) # will print the list in the exact order of the list

tags.sort() # to sort in alphabetical order-the sorta function sorts it
print(tags)

tags.sort(reverse=True) #pass an argument and set true for reverse to work-this is for the list to be returned alphabetical in reverse
print(tags)

totals = [234, 1, 5654, 24234] # a list of totals 
totals.sort() # to sort them in numeric value order
print(totals)