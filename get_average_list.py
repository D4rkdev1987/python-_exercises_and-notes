#can get an average from a list
#very thorough but not great import statistics
#numpy has a mean function-used most often 
#  
# don't use above but use functools reduce
# mean is sum of values divided by number of elements
from functools import reduce

def get_average(num_list):        # function called get_average with num list passed in expecting a list of numbers
    total = reduce(               # get the total here total set equal to reduce
        (lambda total, element: total + element),  # 2 arguments -first lambda total and element--then total added to the element
        num_list                   # second argument is the list to go over
    )

    return total / len(num_list)   # return the total divided by the length of the list
    
num_list = [1, 2, 3, 4, 5, 6]      # list being used 

print(get_average(num_list))      # call get_average and pass in the list


