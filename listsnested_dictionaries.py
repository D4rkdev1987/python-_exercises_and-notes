teams = [               #list containing multiple dictionaries
    {
        'astros': {     #astros is the key
            '2b': 'Altuve',
            'SS': 'Corea',
            '3B': 'Bregman'
        }
    }, 
    {
        'angels': {     #angels is the key
            'OF': 'Trout',
            'DH': 'Pujols'
        }
    }    
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')
# print(angels)
print(list(angels.values())[1])

"""
# when you have nested data structures take 1 at a time
#treated like list and grabbed index 1
#called get on it
#this is key we want
#then grabbed the values into a veiew object
#converted into list
#grabbed whatever we wanted at that point
"""