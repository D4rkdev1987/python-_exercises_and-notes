# merge multiple lists

legacy_customers = ['Alice', 'Bob']      
new_customers = ['Tiffany', 'Kristine']  

raw_db = [legacy_customers, new_customers]  # raw database is equal to combine legacy customers and new customers 
print(raw_db) # this creates2 list inside a list

#-------------------------------------------------------

#combining all strings as seperate elements
#iterating over customer lists and for each loop calling new customers list and tacking on the new elements

for legacy_customer in legacy_customers:  # say for legacy customer in the customers
  new_customers.append(legacy_customer)   # call new customers list and call the append function and then legacy customer

print(new_customers)   # Prints Tiffany Kristine Alice and Bob in one list          