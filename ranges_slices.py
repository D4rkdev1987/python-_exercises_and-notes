tags = [
    'python',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

tag_range = tags[1:-1:2] # we want every other tag here (place in an interval)
tag_range = tags[::-1] #slicing -flip the entire order of the list

print(tag_range)

tags.sort(reverse=True) #sort looks at the alphabetical value

print(tags)