def greeting(first, last):     #greeting is the parent function-with first and last function arguments
  def full_name():             #because it is nested it doesn't need the arguments because it is nested in the greeting function
    return f'{first} {last}'

  print(f'Hi {full_name()}!') # now in the print statement call the full name function here after the format and hi


greeting('Kristine', 'Hudgens') #pass in first and last name here

# when should you nest? whenever you have a function that doesn't need to exist outside a parent function
# example -you never need to call the full_name function.