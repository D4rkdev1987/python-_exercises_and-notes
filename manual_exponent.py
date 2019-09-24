from functools import reduce

"""
manual_exponent(2,3)
#> 8

manual_exponent(10,2)
#> 100
"""
"""
# def manual_exponent(num, exp):
#     counter = exp -1       created a counter variable -1 takes one away (2 x 2 x 2)
#     total = num

#     while counter > 0:
#         total *= num   this will give a product same as total * num
#         counter -= 1   take the counter and decrement it counter is equal to minus 1

#     return total 

# print(manual_exponent(2,3))
# print(manual_exponent(10,2))



#----Functional approach below---------------------------------------------------------------------------
# lambda = an function without a name anonyanous function
reduce iterates over a list and then runs whatever process you tell it to run,
in this case its the lambda function- and keeps the state
"""
def manual_exponent(num, exp):
    computed_list = [num] * exp   
    return (reduce(lambda total, element: total * element, computed_list))


print(manual_exponent(2,3))
print(manual_exponent(10,2))    

