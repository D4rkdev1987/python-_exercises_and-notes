tags = ['python', ' development', 'tutorials', 'code']

# # Nope 
# tags[-1] = 'Programmer'
# print(tags)
#-------------------------------------
#tags.extend('programming')      extend is a function to add on to a list-this will spread out the string elements P r o g r a m
# tags.extend(['programming'])   extend is a function to add on to a list-wrap the string in  it's own element [Programming] which will add it 

#extend is adding to existing list
#extend does not return a new value ery similar to sort function
#--------------------------------------
new_tags = tags + ['Programming'] # set it equal to tags plus and then make it it's own element by ['Programming']
print(new_tags)

#this just allows you to tac on new elemnts and doesn't alter the original
#--------------------------------------

