teams = [               #list containing multiple dictionaries
    {
        'astros': {     #astros is the key with a nested dictionary inside
            '2b': 'Altuve',
            'SS': 'Corea',
            '3B': 'Bregman'
        }
    }, 
    {
        'angels': {     #angels is the key with a nested dictionary inside
            'OF': 'Trout',
            'DH': 'Pujols',
        }
    }    
]

# print(teams) prints a list of mulitple dictionaries
# print(teams[0])   to grab the astros team-returns a dictioary with a single value pair

angels = teams[1].get('angels', 'Team not found') # create a variable angels and then teams and 1st elemnt and get the angels with a default message
# print(angels) prints out outfielder and the DH

print(list(angels.values())) #returns Trout and Pujols
print(list(angels.values())[1])  #returns Trout

"""
# when you have nested data structures take 1 at a time
#treated it like list and grabbed index 1
#called get on it
#this is key we want

#then grabbed the values into a view object
#converted into list
#grabbed whatever we wanted at that point
"""