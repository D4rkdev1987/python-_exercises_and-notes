def greeting(name = 'Guest'):   # default argument is "guest" in here
      print(f'Hi {name}!')      # defualt is for if someone comes on your page without a name for example

greeting()
greeting('Kristine')

# Nope and VERY WRONG WAY
def some_function(collection = []):  # function some_function passed in a collection that expects a list
  collection.append(1)         # call collection.append(1)--this goes to our collection and appends #1
  print(id(collection))      # print the id(place in memory on computer) for the collection
  return collection          


print(some_function())
print(some_function())
