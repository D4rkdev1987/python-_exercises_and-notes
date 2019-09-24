def greeting(name = 'Guest'):   # default argument is "guest" in here
      print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope and VERY WRONG WAY
def some_function(collection = []):
  collection.append(1)         #this goes to our collection and appends #1
  print(id(collection))
  return collection


print(some_function())
print(some_function())
