# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

#first create a variable called a uri(simliar to url)
#now for the search terms, place them in the tags and create a list with a set of strings query terms
#now create a new variable called formatted tags- leverage the join 
#join is a string based function
#add the string which is the plus, then call join and pass in an argument (tags)
#create a new variable query uri  formatted tag  
#we made a list combined them and then formatted with uri


print(query_uri)