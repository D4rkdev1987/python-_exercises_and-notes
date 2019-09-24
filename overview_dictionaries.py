"""
# key value data store
# instead of working with an index
# with a dictionary we use a key value
# we pass in a key to get the value
"""
players = {         #dictionary stored  
    "ss": "Correa", #created a key of ss value of Correa
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer",
}

second_base = players['2b'] # to query

print(second_base)