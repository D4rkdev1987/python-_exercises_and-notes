tags = [             #list created here
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
]

# print(tags[1:4:2])  #this prints code and development

slice_obj = slice(1, 4, 2) #slice object here with a number of arguments- go to 4th element and step to be 2-good to define 
print(tags[slice_obj]) # prints development and code
#-------------------------------------------------------------------
print(slice_obj.start)# finding where the range starts 
print(slice_obj.stop) # finding where the range stops
print(slice_obj.step) # finding the intervals the program is being returned

#--------------------------------------------------------------------
# slice_obj = slice(2)
# print(tags[slice_obj]) # call tags and pass in slice_obj-will return python and development-you can call and store the method and store in another variable and call anywhere in the program

# whenever you want to define your ranges and steps and calls them in a variable
# and call them later on and call different data steps
