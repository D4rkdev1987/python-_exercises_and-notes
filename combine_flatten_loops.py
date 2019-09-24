"""
2 list and we want to combine them---
append is in the list data type---
utilized for in loop
iterating through Alice and Bob and with each loop calling new customers list
and then append the new_customers
"""

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db) # this creates2 list inside a list

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)