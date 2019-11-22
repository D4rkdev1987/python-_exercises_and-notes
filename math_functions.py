import math
#create 2 variables
loss = -20.25 #floating point number
product_cost = 89.99 #floating point number
#absolute or abs value removes the negative here

print(abs(loss)) #abs = absolute value of loss-takes pure value and removes the negative sign 
print(math.floor(product_cost)) # returns 89 rounded down value-math floor returns an integer-you can call int as well
print(math.ceil(product_cost))   # returns 90 upper rounded value-math ceiling-rounds up to next whole number
print(abs(math.floor(loss)))  #math floor is called first then the absolute value 21
print(round(product_cost)) #rounding to the nearest whole number 90-simply round to the nearest whole number
print(math.sqrt(product_cost)) #brings back a floating point number-square root-9.486305919
print(math.pow(5, 2)) # this is squared here 5 x 5 returns floating point number 25.0
print(5 ** 2)  # same is above but returns 25 returning the integer