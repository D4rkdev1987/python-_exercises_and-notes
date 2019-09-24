teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge","Stanton"],
    "red sox": ["Price", "Betts"],
}

featured_team = teams.get('mets', 'No featured team')
#get takes 2 arguments takes the key and then the value
#key look up in case that it doesn't exist
print(featured_team)

