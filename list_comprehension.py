"""
we can set a number for in loops to function on a single line 
and generate list from those lines of code

set of 'for in loops' and conditionals placed in a single line of code
"""

num_list = range(1, 11)  # create the num list and say range and you want numbers 1-10
cubed_nums = []          # get the cubed numbers(take all nmbers and cube them)

for num in num_list:          # for num in the the num list
  cubed_nums.append(num ** 3) # cubed nums and append and say num ** 3 which cubes the values

print(list(num_list))
print(cubed_nums)

# synatx below is basically the same as above
#--------------------------------------------------------------------
cubed_nums = [num ** 3 for num in num_list]  # 3 seperate components here  (num can be x or b or anything it's your iterator variable)
                                             # first is the action we want to take and then place in the for in loop (num is iterator variable and can be anything)
                                             # the brackets say you want to generate a list when wrapped in  square brackets [ ]
print(cubed_nums)

"""
call cubed nums need to store it in a value and store it in square brackets
first item is action/value inside list so first item is ** 3 the for num in the num list
'we are auto generating the list'
'num is iterator value'
'square brackets dynamically generates the list'
"""
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#------------------Making list dynamic using a condition below--------

#list to capture even numbers
num_list = range(1, 11)

even_numbers = []                                         # say even numbers equals a is eqqual to empty list

for num in num_list:                                      # condition below
  if num % 2 == 0:                                        # if the num is % (modulus operator tells us if remainder) 2 is equal to zero (is it even)
    even_numbers.append(num)                              # take the even numbers and append the numbers


#list comperhension to have the same behavior below
even_numbers = [num for num in num_list if num % 2 == 0]  # start with square brackets then num for num in the list, then add the condition on the same line

print(even_numbers)

# num is the first element-python says what ever element we are returning is the one we want to add(only if it is even)
"""
start with square brackets to geneertae the list
just combine the condition on the same line
when you use a conditional ( 3 elements before now 4)
if num % 2 == 0 is the condition
"""
