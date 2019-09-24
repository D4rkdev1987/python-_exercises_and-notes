from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

print(int(product_cost))  #returns 88 not 88.80 and takes away the .80
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))