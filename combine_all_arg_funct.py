"""
#list of steps 

# start with a positional arg and give a single star for the name and then double star for kwargs (print greeting to user and go through key value pair)         
# print-formatted string-inside string literal join statement and takes in full set of args(first name last name ect)
#       then pass in time of day and end for greeting
# check to see if there are any keyword args print out task list implementing a loop here
# for the key and the value in the key word arg (can't loop over dictionary itself) kwargs.itms
# print formatted key and value
# 
# call the greeting when passing in a large number of arguments list them on different lines
# now place in the name kristine and last name hudgens
# no for the args the unpacked- first dish washer, second puupper outside and third is homework
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



