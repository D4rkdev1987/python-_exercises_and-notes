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
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)

# tags in tags_two but not in tags_one
exclusive_to_tag_two =  tags_two - tags_one
print(exclusive_to_tag_two)

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)