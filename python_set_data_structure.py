# Uniqueness
tags = {      # list of tags----
  'python',
  'coding',
  'tutorials',
  'coding'        # the second coding will not print out in the terminal
}

print(tags) # prints a set syntax-set requires that everything in the set is unique-don't want duplicates

# Nope
print(tags[0])  # will not work-sets do not support indexing

#to query a set
query_one = 'python' in tags 
query_two = 'ruby' in tags

print(query_one) # will print true-won't give the element-what we are saying here is, "is python in tags"
print(query_two) # same as above but will return false