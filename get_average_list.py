#can get an average from a list
#thorough import statistics
#numpy has a mean function
# don't use above but use functools reduce
# mean is sum of values divided by number of elements
from functools import reduce

def get_average(num_list):
    total = reduce(
        (lambda total, element: total + element),
        num_list
    )

    return total / len(num_list)
    
num_list = [1, 2, 3, 4, 5, 6]

print(get_average(num_list))


