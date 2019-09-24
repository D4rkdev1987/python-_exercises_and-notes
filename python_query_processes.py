tags = ['python', 'development', 'tutorials', 'code'] # database query here
#big difference between index and length---index starts with 0 ---length starts with 1
number_of_tags = len(tags)
last_item = tags[-1] #value of the last item using negative index
index_of_last_item = tags.index(last_item) #once you have value you can pass to the index function and return of value

print(number_of_tags)
print(last_item)
print(index_of_last_item)


