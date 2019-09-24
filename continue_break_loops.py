"""
build a loop to search for a name and alter behavior 
conitnue  ///// Break        <----flow operators
first loop--Continue  ###############################################
in the loop block reference every value 

print and format and say sorry-whatever username is, not allowed
continue in a loop if it finds a condition it keeps on going
############################################################
second loop--Break   ##############################################
break looks through list of users just finds user name and stops

print and format and call the user name and say was at index
then call user name and use index
now say break 
"""

usernames = [           #list of user names here
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)