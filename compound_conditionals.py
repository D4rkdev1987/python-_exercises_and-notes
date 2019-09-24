# username = 'jonsnow'
# email = 'jon@email.com'  #variables in string value
# password = 'thenorth'

# #need to items true
# # and operator

# if username == 'jonsnow' and password == 'thenorth': #joining conditions-everythong on left and right have to be true
#   print('Access permitted')
# else:
#     print('you shall not pass')    

# # or operator allows you to use either username and or password--as long as one side matches up    

logged_in = True
stadard_user = True

if logged_in and not stadard_user:  # if statement can only look at one item! and not though--right side is false
    print('You can access the admin')
else:
    print('You can only access the standard dashboard')    