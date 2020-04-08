post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))               #both id's are the same- id's - gives you a reference and unique id from memory
print(id(post))

post += ('published',)        #setting value using mass assignment operator

print(id(post))               #this id overrides id in memory
#---------------------------------------------------------
# post = post + ('published), #concatinating( adding 2 together) ---place the value in first('published',) can't forget the comma for tuples
# title, sub_heading, content, status = post

# post += ('published',)      #setting value using mass assignment operator

# print(title)
# print(sub_heading)
# print(content)
# print(status)
#---------------------------------------------------------
