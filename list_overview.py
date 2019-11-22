"""
User Database Query
Kristine
Tiffany                 #  <------multi line list
Jordan
"""
#lists in python is like an array a collection of values you can query and remove items and add items
#lists/arrays in python are not immutable 

users = ['Kristine', 'Tiffany ', 'Jordan'] # stored in a variable called users 

print(users)

users.insert(0, 'Anthony')   #use insert to place new names into list at specific index

print(users)

users.append('Ian') #this is just adding the name to the end of the list by using append

print(users[2])   #querying an element-how to get access to one of the items-when you query a specific item it won't return brackets

users[4] = 'Brayden' # to reassign a name in the list, not changing the string

print(users) # prints a set of strings