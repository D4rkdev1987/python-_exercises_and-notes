def greeting(first, last):     #greeting is the parent function
  def full_name():             #because it is nested it doesn't need the arguments
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens') #pass in first and last name here

# when should you nest? whenever you have a function that doesn't need to exist outside a parent function