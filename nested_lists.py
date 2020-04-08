users = ['Kristine', 'Tiffany', 'Jordan', 'Leann'] # list of strings
ids = [1,2,3,4] # list of integers 

mixed_list = [42, 10.3, 'Altuve', users] # first element is an integer, then a float, then a string, then call users to slide the list of users
                                        # dangerous list-be careful on using using mixed list data types
print(mixed_list)

user_list = mixed_list.pop() # will pop off the list users and print all the list names

print(user_list)
print(mixed_list)

nested_list = [[123], [234], [345]] 