
def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'
  

print(heading_generator('Greetings!', '1'))
print(heading_generator('I am in a title', '3'))
