#regular expressions allows you to match files
#pulled in fnmatch library to pass in the regular expressiosn(if text we go over if anything matches the .txt or .rb. .yml)
import fnmatch                               
from fnmatch import fnmatchcase    #matchcase here it is possible to be extended by matchcase          
import os                                    

def list_files():                            # create a function list_files
    for file in os.listdir('.'):             # create the for in loop say os.listdir to access the directory '.' will loop through every file 
        if fnmatch.fnmatch(file, '*.txt'):   # calling the module fnmatch and the function fnmatch pass 2 args (name what ever to loop through, and then '*.txt)
            print('Text files:', file, "\b") # now print text files and file

        if fnmatch.fnmatch(file, '*.rb'):    #calling the module fnmatch and the function fnmatch pass 2 args (name what ever to loop through, and then '*.rb)
            print('Ruby files:', file)       #now print Ruby files and file

        if fnmatch.fnmatch(file, '*.yml'):   #calling the module fnmatch and the function fnmatch pass 2 args (name what ever to loop through, and then '*.yml)
            print('Yaml files:', file)       #now print Yaml files and file

        if fnmatch.fnmatch(file, '*.py'):    #calling the module fnmatch and the function fnmatch pass 2 args (name what ever to loop through, and then '*.py)
            print('Python files:', file)     #now print Python files and file


list_files()                                 # call list files
#---------------------------------------------------------------------------------------------------------
players = [                                  # create a list of baseball players here
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]
# go through player array and filter down and if 2nbase is found filter it out and just grab those elements
second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]   # say second base players (to loop through) say player for player in players
                                                                                      # now the condition (in players) if fnmatchcase then pass in string of player and *2B
print(second_base_players)                                                            # now print the second_base_players variable