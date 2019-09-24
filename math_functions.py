import math
#create 2 variables
loss = -20.25
product_cost = 89.99 #floating point number
#absolute or abs value removes the negative here

print(abs(loss))
print(math.floor(product_cost)) # returns 89 lower rounded value
print(math.ceil(product_cost))   # returns 90 upper rounded value
print(abs(math.floor(loss)))  #math floor is called first then the absolute value 21
print(round(product_cost)) #rounding to the nearest whole number 90
print(math.sqrt(product_cost)) #brings back a floating point number
print(math.pow(5, 2)) # this is squared here 5 x 5 returns floating point number 25.0
print(5 ** 2)  # same is above but returns 25