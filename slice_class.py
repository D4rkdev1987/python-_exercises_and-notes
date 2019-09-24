tags = [             #list created here
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
]

# print(tags[1:4:2])  #this prints code and development

slice_obj = slice(1, 4, 2) #slice object here with a number of arguments
print(slice_obj.start)
print(slice_obj.stop)
print(tags[slice_obj]) # call tags and pass in slice_obj
# whenever you want to define your ranges and steps and calls them in a variable
# and call them later on and call different data steps
