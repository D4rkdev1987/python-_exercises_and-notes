from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

print(int(product_cost))  #returns 88 not 88.40-takes floating point variable and throws it away 
print(float(qty)) # returns 450.0
print(Decimal(product_cost)) # returns 88.799999999999715
print(complex(commission_rate)) # (0.8+oj) scientific notation

# first example we take the product cost and convert it to an integer
# use float and pass in the quantity
# next we converted the product cost to a decimal by using Decimal and by pulling in the decimal library
# for the comission rate we are getting the scientific notation for 0.08 by using complex