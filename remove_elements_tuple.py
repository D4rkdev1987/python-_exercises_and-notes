# a tuple is not able to be changed -immutable
# here we create a new tuple 

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
#leverageing ranges 
#implement reassignment
# make it equal to a range and make a new tuple (still can use post variable)
# create the slice don't pass anything in as first arg
#brings in slice of element 1 2 3 and stop before last one

post = post[:-1]
#---------------------------------------------------------
# Removing elements from beginning
# just remove the second argument 
# only grab elements and skip first element

post = post[1:]
#---------------------------------------------------------
# Removing specific element (messy/not recommended)
# perform reassignment
# convert into a list
# casting post into list 
# now you have a list, you can remove items ('published remove)
# to finish it perform reassignment and cast back into tuple
# create a new variable called post 

post = list(post)
post.remove('published')
post = tuple(post)

print(post)