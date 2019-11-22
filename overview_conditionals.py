# Single condition
age = 25   # variable called age 

if age < 25:     #this is the condition here (if is a reserved word)
  print(f"I'm sorry, you need to be at least 25 years old")
 #-------------------------------------------------------------------

# if/else
age = 55   # variable age 

if age < 25:    # reads if the age is less than 25
  print(f"I'm sorry, {age} is under 25 years old")   # if the age is less than 25 or if it is true this happens
else:
  print(f"You're good to go, {age} fits in the range to rent a car")  # this is if the condition is not true this would run 
# --------------------------------------------------------------------

# if/elif/else
age = 55

if age < 25:    #condition
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100: #condition else if statement 
  print(f"I'm sorry, {age} is over 100 years old")
else:           # else statement
  print(f"You're good to go, {age} fits in the range to rent a car")