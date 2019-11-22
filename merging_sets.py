"""
2 sets of tags 
create a variable called merged tags and assign to tags one
use the pipe character-it merges the sets together

###############
to have a master type of set and subtracting other items
its subtracts the duplicates when called tags_one it prints python
exclusive_to** 
###############
universal_tags only prints out the similar elements 
must use the ampersand symbol
"""

tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# merged tags
merged_tags = tags_one | tags_two
print(merged_tags)

# tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two  # just say tags one minus tags two returns only python
print(exclusive_to_tag_one) # you are looking for what tags belong only in tags 1(example a vendiagram)-and ignores ruby and development

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)  # prints ruby and development-they are the only 2 elements in tag 2 and not tag 1

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two # gettingonly the shared items
print(universal_tags) # will return coding and tutorials-only shared elements