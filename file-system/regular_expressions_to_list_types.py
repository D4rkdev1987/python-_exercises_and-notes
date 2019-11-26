import fnmatch                   # import fnmatch(built into python)
from fnmatch import fnmatchcase  # from fnmatch import fnmatch case
import os                        # import os

def list_files():                    # function called list files
    for file in os.listdir('.'):             # loop for file in os in operating system list directory (. is this directory)
        if fnmatch.fnmatch(file, '*.txt'):    # reg expression- if fn match.fnmatch(call module library)-2 args name of what we loop through first-and then a string("*txt")
            print('Text files:', file, "\b")  # now print the Text Files, pass in the second argument file

        if fnmatch.fnmatch(file, '*.rb'):     # find the ruby file
            print('Ruby files:', file)         

        if fnmatch.fnmatch(file, '*.yml'):    # find the yaml files
            print('Yaml files:', file)

        if fnmatch.fnmatch(file, '*.py'):     # find python file
            print('Python files:', file)      


list_files()
#regular expressions allow you to match patterns
# pulled in the fnmatch library to pass in reg expressions

players = [               # create a list     go through the array players and filter-if 2b is found and grab those elements
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]
# above-created a variable named second base players-now build a list dynamically
# say player for player in the players list(grabbing player item) looping through------
# now conidtion    if fnmatchcase now pass in the player and the second argument say "* 2B"

print(second_base_players)
