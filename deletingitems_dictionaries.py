teams = {                                     ## variable teams
  "astros" : ["Altuve", "Correa", "Bregman"], ## keys and values
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# del teams['astros']                ## to simply delete using the del function
teams.pop('astros', 'No team found') ## similar to the get function, takes in 2 arguments(but will always return the look up)
removed_team = teams.pop('astros', 'no team found here') ## the value of the look up will be returned not the key
#pop returns value of lookup or returns the value of defualt element

print(removed_team)
print(teams)