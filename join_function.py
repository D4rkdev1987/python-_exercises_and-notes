# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q=' # variable uri and paste in link as a string
tags = ['python', 'development', 'tutorial'] # search terms here-a list (query terms)
formatted_tags = '+'.join(tags) # variable formatted_tags- join function is a string based function-plus sign is character then join and pass in the argument
query_uri = f'{uri}{formatted_tags}' # variable query-then string literal syntax with f (format tag) pass in uri and then pass in formatted_tags

print(query_uri)

#first create a variable called a uri(simliar to url)
#now for the search terms, place them in the tags and create a list with a set of strings query terms
#now create a new variable called formatted tags- leverage the join 
#join is a string based function
#add the string which is the plus, then call join and pass in an argument (tags)
#create a new variable query uri  formatted tag  
#we made a list combined them and then formatted with uri

print(query_uri)