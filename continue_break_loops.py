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
#-------------------------------------------------------------
usernames = [           #list of user names here
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:             # say for username in usernames
  if username == 'cersei':             # now if username(referenceing the values) then double equal cersei
    print(f'Sorry, {username}, you are not allowed')    # then print and format(f) Sorry and what the username is and is not allowed
    continue                           # then continues on to the next- if it finds the condition/the username and tells program to continue through loop
  else:
    print(f'{username} is allowed')    # if it isn't the name then they are allowed is what this line means

for username in usernames:        
  if username == 'cersei':        #
    print(f'{username} was found at index {usernames.index(username)}')   # print format username was found, then in the brackets and call the usernames and use the index and pass in the username
    break                         # it will stop at cersei-it finds it and then does not continue the loop 
  print(username)