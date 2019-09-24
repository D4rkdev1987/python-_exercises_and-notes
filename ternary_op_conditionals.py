# allows youto create an if else statement
# web application that needs auth
# you can access if role is set to admin if not you cannot


role = ' admin' #variable role

# ternary operator
auth = 'can access' if role == ' admin' else 'cannot acces'
                    #conditional above
print(auth)

# traditional syntax below
if role == 'admin':
    'can access'
else:
    auth = "cannot access"    

