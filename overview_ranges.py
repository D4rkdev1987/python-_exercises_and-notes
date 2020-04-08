#RANGES
# takes in 2 arguments where to start and where to end

tags = ['python', 'development', 'tutorials', 'code'] #list of tags with 4 elements stored in variable

tag_range = tags[1:2]#the range stops at turtorials-go from first to second-second argument is not included in the result
tag_range = tags[1:] #starts at development and ends with code
tag_range = tags[:2] # only returns python and development
tag_range = tags[:-1] #bring all elemnets except at the very end element
tag_range = tags[:] #pass all elements in 

print(tag_range)