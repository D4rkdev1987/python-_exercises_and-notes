post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')
print(post[:2])
print(post[1::2])

#created a print statement called post
#grab firtst element (first expression)
#pass in the index of 2
#returns a tuple of the first 2 elements
print(post[1::2])
#because of index of 2 being selected it skips over
### the cool python content and returns published

#whwnever you run a slice in a tuple it ruturns the same 
#data struture meaning it returns as a tuple