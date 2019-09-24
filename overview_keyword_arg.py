# this takes in a keyword list as an argument (combining names arguments) 

def greeting(**kwargs):     # 2 stars followed by kw-keyword
      print(kwargs)


greeting()                  # this returns a dictionary with no arguments
greeting(first = 'Kristine', last = 'Hudgens')   # now insert named arguments (this returns a dictionary)

def greeting(**kwargs):
  if kwargs:              # implementing a conditional starting--check if kwargs were set or not
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!") # for dictionary pass in bracket syntax using []
  else:                   # if no keyword args were given
    print('Hi Guest!')    # just say hi guest


greeting()
greeting(first = 'Kristine', last = 'Hudgens')