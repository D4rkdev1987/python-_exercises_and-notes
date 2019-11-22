# allows youto create an if else statement
# web application that needs auth below
# ternary operator- condition true will go first
# auth in the ternary operator is use it once in the beginning instead of a conditional using it multiple times


role = ' admin' #variable role-user admin logged in

# ternary operator
auth = 'can access' if role == ' admin' else 'cannot acces' # vairable auth to store output of ternary operator
                                                            # say can access if role is equal to admin else (if not) cannot access
print(auth)
#-----------------------------------------------------------

# traditional syntax below---basic conidtional similar to above but without ternary 
if role == 'admin':   # if the role is equal to admin
    'can access'      #they can access
else:                      # if not 
    auth = "cannot access"    # authentication is they cannot access

