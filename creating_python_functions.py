def full_name(first, last):       # start with def(define) called full name(use snake case), then end with perentheses then function arguments and a colon just like conditionals
  print(f'{first} {last}')        # proper indentation--print format first and last
                                  # 2 lines under the print and this is structure for it

full_name('Kristine', 'Hudgens')  # you need to have 2 positional arguments--supplied the elements to be rendered here

#-------------------------------------------------------------------
#-----------More Complex below--------------------------------------

def auth(email, password):                                       # auth takes a couple arguments here- email and password
  if email == 'kristine@hudgens.com' and password == 'secret':   #intgrate a conditional--if email is equal to Kristine email and password is equal to secret
    print('You are authorized')                                  # print our authorized
  else:
    print('You are not authorized')    


auth('kristine@hudgens.com', 'asdf')     # this is where you are calling the function and passing in the arguments

#-------------------------------------------------------------------
#-------------Function with no arguments with loop------------------
#No Arguments 
def hundred():                    # hundered takes no arguements here
  for num in range(1, 101):       # this is a for in loop--creates a range from 1 to 100
    print(num)                    


hundred()
#--------------------------------------------------------------------
#--------------------------------------------------------------------

def counter(max_value):           # counter takes in one argument max value-dynamic value
  for num in range(1, max_value):
    print(num)


counter(501)