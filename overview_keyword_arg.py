# this takes in a keyword list as an argument (combining names arguments) 

def greeting(**kwargs):                          # 2 stars followed by kw-keyword arguments
      print(kwargs)


greeting()                                       # this returns a dictionary with no arguments-difference beteween *args(unpacking) is args returns a tuple
greeting(first = 'Kristine', last = 'Hudgens')   # now insert named arguments (this returns a dictionary) first is the key and kristine would be value

def greeting(**kwargs):
  if kwargs:                                                           # implementing a conditional starting--check if kwargs were set or not
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!") # for dictionary pass in bracket syntax using []
                                                                       # pass in bracket synatx pass in the first name and then same as last name
  else:                                                                # if no keyword args were given
    print('Hi Guest!')                                                 # just say hi guest


greeting()   # Hi guest have a great day
greeting(first = 'Kristine', last = 'Hudgens')