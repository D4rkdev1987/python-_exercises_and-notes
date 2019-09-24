# this is newer version 
# view objects allow you to peak in to view keys and values

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
# player_names = list(players.copy().values())


# print(players.keys())
# print(list(players.values())) #cannot view object like a list
# # print(players.items())

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}


team_grouping = teams.items()
print(list(team_grouping)[1][1][0] )  #to find the index of angels use )[1])
#if you have a dictionary and elements and you want to grab a nested 
#items

#we casted as a list an casted values
#we grabbed the angels 1
#then we wanted to get to the players
#then we wanted trout so we put in trout

"""
[('astros', ['Altuve', 'Correa', 'Bregman']), 
('angels', ['Trout', 'Pujols']), 
('yankees', ['Judge', 'Stanton']), 
('red sox', ['Price', 'Betts'])]
"""