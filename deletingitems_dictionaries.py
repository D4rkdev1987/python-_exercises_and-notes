teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# del teams['astros']
removed_team = teams.pop('astros', 'no team found here') #pop returns value of lookup or defualt element

print(removed_team)
print(teams)