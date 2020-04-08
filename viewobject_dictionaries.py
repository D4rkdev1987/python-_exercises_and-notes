# this is newer version 
# view objects allow you to peak in to view keys and values and all the items

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
# print(players.keys())          ##this prints dict_keys and the the keys wrapper in parens (this means there is an object or in this case dictionary view object)
# print(players.values())
# print(players.values()[0])     ##cannot treat view objects like a list-this returns an error*********
# print(players.items())
# everytime we run a query it runs on a thread***


# print(list(players.values())[1]) ##cannot view object like a list-cast it as a list here to return the list value

# to copy the list-for thread safe programming
# player_names = list(players.copy().values()) - using the copy function correa Altuve Bregan Gattis Springer, accessed only by us 
# print(player_names)



#nested items now below
teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}


team_grouping = teams.items()    # teams dictionary object-returns a set of tuple items
print(len(team_grouping))        # returns 4 items
print(list(team_grouping))       # converts to a list that contains tuples inside of it
"""
[('astros', ['Altuve', 'Correa', 'Bregman']), 
('angels', ['Trout', 'Pujols']), 
('yankees', ['Judge', 'Stanton']), 
('red sox', ['Price', 'Betts'])]
"""
print(list(team_grouping)[1])         # returns (angels, ['Trout', 'Pujols']) because they are index 1
print(list(team_grouping)[1][1])      #returns Trout and Pujols to get to the players array
print(list(team_grouping)[1][1][0])   # returns Trout to get the player
