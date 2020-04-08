def full_name(first, last):
      print(f'{first} {last}')


full_name('Kristine', 'Hudgens')                 # Kristine is passed to first argument and Hudgens is passed to the second argument

# Named Arguments
full_name(first = 'Kristine', last = 'Hudgens')  # pass in the first name variable and last name variable to kristine and hudgens
full_name(last = 'Hudgens', first = 'Kristine')  

# because named arguemnts declare the mapping you can set the order you prefer 
# python- if there are more than 2 arguments use NAMED ARGUEMENTS