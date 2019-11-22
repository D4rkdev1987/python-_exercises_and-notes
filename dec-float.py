from decimal import Decimal   # importing from python

product_cost = 88.40
commision_rate = 0.08
qty = 450

product_cost += (commision_rate * product_cost)
print(product_cost * qty)     #42962.4

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

product_cost = Decimal(88.40) # Decimal is a function so the number 88.40 is no longer a floating point it's a decimal
commision_rate = Decimal(0.08)
qty = 450

product_cost += (commision_rate * product_cost)
print(product_cost)        #42962.40000000000282883716451

