post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))             #both id's are the same
print(id(post))

# #post = post + ('published), #concatinating ( adding 2 together)
post += ('published',)      #setting value using mass assignment operator

print(id(post))  #this id overrides id in memory

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)
