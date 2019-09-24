"""
we can set a number for in loops on a single line 
and generate list from those lines of code
set of 'for in loops' and conditionals 
"""

num_list = range(1, 11)
cubed_nums = []
"""
want to return every element cubed
starts off as an empty list
"""
for num in num_list:
  cubed_nums.append(num ** 3)
"""
you say cubed nums and append it 
then num ** 3 cubes each number in the list
"""
#############################################
cubed_nums = [num ** 3 for num in num_list]
"""
call cubed nums need to store it in a value and store it in square brackets
'we are auto generating the list'
'num is iterator value'
'square brackets dynamically generates the list'
first item is action/value inside list
for num in numlist after
"""
print(cubed_nums)
#############################################
"""
dynamically generate a different list
'you only want to get even numbers'
first you say even number with an empty list
the set your for in loop


"""
even_numbers = []

for num in num_list:
  if num % 2 == 0:   # is it even 
    even_numbers.append(num)  

even_numbers = [num for num in num_list if num % 2 == 0]
"""
start with square brackets to geneertae the list
just combine the condition on the same line
when you use a conditional ( 3 elements before now 4)
if num % 2 == 0 is the condition
"""
print(even_numbers)