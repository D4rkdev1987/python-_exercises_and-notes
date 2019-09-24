def full_name(first, last):       # start with def(define) called full name(use snake case), then end with perentheses then function arguments and a colon just like conditionals
      print(f'{first} {last}')    # proper indentation--print format first and last
                                  # 2 lines under the print and this is structure for it

full_name('Kristine', 'Hudgens')  # you need to have 2 positional arguments--supplied the elements

def auth(email, password):        # auth takes a couple arguments here
  if email == 'kristine@hudgens.com' and password == 'secret':   #intgrate a conditional--
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():                    # hundered takes no arguements here
  for num in range(1, 101):       # this is a for in loop--creates a range from 1 to 100
    print(num)                    


hundred()

def counter(max_value):           # counter takes in one argument max value
  for num in range(1, max_value):
    print(num)


counter(501)