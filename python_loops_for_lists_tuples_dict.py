players = ['Altuve', 'Bregman', 'Correa', 'Gattis'] #basic lists of strings here
players = ('Altuve', 'Bregman', 'Correa', 'Gattis') # this is a tuple

for player in players:    # say for and then (iterator or block variable, can be anything ) player in players--common convention for iterating over a collection
  print(player)           # prints the names ( each time loop goes through it changed the value of the variable)
#------------------------------------------------------------------
players = {         # dictionary
  '2b': 'Altuve',
  '3b': 'Bregman',   # key value pairs
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():  # say for and then 2 words (position(starts) player(sencond)) then players.items()--items creates a veiw/access 
  print('Position', position)             
  print('Player', player)                 