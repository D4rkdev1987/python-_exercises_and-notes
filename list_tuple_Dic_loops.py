"""
using the for in loop
whenever you are itterating over the player is the iterator variable
each time the loop goes through it goes through each 
common convention is if you have a plural name for the variable make the iterator variable(block variable) singular
####################################
if changed to a tuple it will work the same way
####################################
in a key value dictionaries
set the key value pairs
to grab the key and value say for position player in players and cal the items function
items function allows you to view and can pass in 2 variables
the first item (block variable) is set to 2b and the second is Altuve

"""
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)