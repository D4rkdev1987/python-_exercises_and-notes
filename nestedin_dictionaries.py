"""
#nested collections
#when you break elements down in lowest form
#you know what element and how to work with them
"""
teams = {   #-->variable named teams -->assignment operator = 
    "angels": [" Trout", "Pujls"],
    "yankees": ["Judge", "Stanton"], 
    "astros": ["Altuve", "Correa", "Bregman"], #list here-single element inside teams
}

astros = teams['astros']
print(astros)
print(['astros'][:2]) #slices altuve
print(['astros'][2])  #Bregman