post = ('Python Basics', ' intro to python', 'some cool python content')

#add a new element at the end with a list  of tags inside-a tuple of nested strings with a list inside  BELOW!

tags = ['python', 'coding', 'tutorial']   #list called tags with strings in the list

post += (tags,)#to update reassignment (tuple)-use assignment operator and place in "tags," (because tags is stored in a variable)
# above will simply print the tuple with the list inserted at the end
print(post[-1])#to get the list 

print(post[-1][1])#prints the 1 index 'coding'