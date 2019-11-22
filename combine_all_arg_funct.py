"""
#list of steps 

# FUNCTION- start with a positional arg time of day and give a single star for the name and then double star for kwargs (behavior we are looking for print greeting to user and go through key value pair)         
# GREETING- print-formatted string-inside string literal join statement and takes in full set of args which takes in the users(first name last name ect)
#       then pass in time of day and end for greeting
# IF -check to see if there are any keyword args print out task list implementing a loop here
# FOR -for the key and the value in the key word arg (can't loop over dictionary itself) kwargs.itms
# print formatted key and value
# 
# call the greeting when passing in a large number of arguments list them on different lines
# now place in the name kristine and last name hudgens -set of items -tuple arguments
# now for the args unpacked- first dish washer, second puupper outside and third is homework --key word arguments
"""

def greeting(time_of_day, *args, **kwargs):
      print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

      if kwargs:
        print('Your tasks for the day are:')
      for key, val in kwargs.items():
        print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')



