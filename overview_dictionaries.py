"""
# key value data store-you can create a key with a value related
# instead of working with an index # with a dictionary we use a key value
# we pass in a key to get the value
"""
players = {         #dictionary stored in players variable
    "ss": "Correa", #created a key of "ss", value of "Correa"
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer",
}

second_base = players['2b'] # to query- to grab the second base player-call the players dictionary then just pass in the string value of the key

print(second_base)

# remember what ever string based key is IDENTICAL MATCH TO THE KEY in the dictionary