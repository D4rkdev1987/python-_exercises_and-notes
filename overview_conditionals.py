# Single condition
age = 25

if age < 25:     #this is the condition here
  print(f"I'm sorry, you need to be at least 25 years old")

# if/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

# if/elif/else
age = 55

if age < 25:    #condition
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100: #condition
  print(f"I'm sorry, {age} is over 100 years old")
else:           #condition
  print(f"You're good to go, {age} fits in the range to rent a car")