# lambda is a tool allows you to wrap up a smaller function and easily pass it to other functions
# lambda wraps up a process-small behavior and pass it to functions
# similar to a variable
# labmda returns a value-return a full name value

# to create a lambda then a list of arguments first and last name
# then a colon and then what is going to be returned
# (basic function)
#now greeting function
# in the greeting pass in the full name lambda 

# first goes to lambda and pass in two values, and stored in the variable-which allows us to pass into the greeting the function
full_name = lambda first, last: f'{first} {last}'  # variable is full_name


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens')) 