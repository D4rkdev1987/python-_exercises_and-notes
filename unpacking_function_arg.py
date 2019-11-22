# you have a function that needs to take in a collection of data (elements unknown)
# one element or many elements


def greeting(*args):                 # unpacking start with a star(astrix) then name argument list args --unpacked
      print('Hi ' + ' '.join(args))  # concatenate the arguments .join then pass in args(no astrix only needed in the function declaration)
                                     # print(args) -returns a tuple data structure


greeting('Kristine', 'M', 'Hudgens') # call greeting function-3 arguments works the same way as below
greeting('Tiffany', 'Hudgens')

#------------------------------------------------------------
#------------------------------------------------------------

def greeting(*names):                # doesn't have to be args can be names--BUT NOT PYTHON BEST PRACTICE
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')

#------------------------------------------------------------
#------------------------------------------------------------


def greeting(time_of_day, *args): #positional argument first then pass in the arguments(args)
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}") # join takes in a collection-joins it-turns into a string and places a space
                  #wrapping the join in the curly brackets like it is above { } is using string literal remember

greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')


