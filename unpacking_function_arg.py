# you have a function that needs to take in a collection 
# one element or many elements


def greeting(*args):                 # unpacking start with a star then name argument list args
      print('Hi ' + ' '.join(args))  # concatenate the arguments .join args


greeting('Kristine', 'M', 'Hudgens') # call greeting function
greeting('Tiffany', 'Hudgens')


def greeting(*names):                # doesn't have to be args can be names--BUT NOT PYTHON BEST PRACTICE
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args): #positional argument first then pass in the arguments(args)
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')


