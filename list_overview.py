"""
User Database Query
Kristine
Tiffany                 #  <------multi line list
Jordan
"""
#lists in python is like an array a collection of values you can query and remove items
#lists/arrays in python are not immutable 

users = ['Kristine', 'Tiffany ', 'Jordan'] 

print(users)

users.insert(0, 'Anthony')   #use insert to place new names into list at specific index

print(users)

users.append('Ian') #this is just adding the name to the end of the list

print(users[2])   #querying an element 

users[4] = 'Brayden'

print(users)