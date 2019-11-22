teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge","Stanton"],
    "red sox": ["Price", "Betts"],
}

featured_team = teams.get('mets', 'No featured team') #call the teams dictionary first then get which get takes 2 arguments takes the key and then the value, with a default value
#key look up above doesn't exist so it will print No Featured team

print(featured_team)

