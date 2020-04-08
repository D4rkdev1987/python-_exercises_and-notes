#lists uses []
#dictionary uses {}
#tuple uses ()

#Tuple: immutable-- tuple not sortable-cannot be changed
#List: mutable-can be changed

post = ('Python Basics', 'Intro guide to python', 'cool python content here')  #tuple

title, sub_heading, content = post #unpacking done here-python treats each item as a query engine
# Equivalent to Tuple unpacking below

# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)

