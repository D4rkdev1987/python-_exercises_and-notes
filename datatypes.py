meal_completed = True  # <--boolean value is always true or false value(is published or not example) use Captital T for true and F for false
sub_total = 100  # <--standard number here equal to 100
tip = sub_total * 0.2  # <--floating point number 0.2(floats and integers are in the number data type)
total = sub_total + tip  # <--this says the total is equal to the sub_total plus the tip
receipt = "Your total is " + str(total) # <--want the reciept with a string plus the str(string) and pass in the total in parens
print(receipt) 


# Booleans- true or false value
# Numbers- anything from standard integers all the way to decimals and floating point numbers (can be connected to number based libraries)
# Strings- wrapper with single or double quotation marks (name, html doc ect)
# Bytes and byte arrays-used in tasks such as images on byte level 
# None-if define a variable but you don't want to set the value yet, you use none
# DATA STRUCTURE CATEGORY BELOW
# Lists-managing collections-similar to an array gives a list of items
# Tuples-managing collections
# Sets-managing collections
# Dictionaries-managing collections-gives ability to have key value pairs