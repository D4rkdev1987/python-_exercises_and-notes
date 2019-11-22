#ability to create a function heading generator and takes in a title and heading type
def heading_generator(title, heading_type):                 # create the function heading generator-takes in a title and heading type
      return f'<h{heading_type}>{title}</h{heading_type}>'  # return a formatted string start off by saying <h say heading type> returns a string of <h1>
                                                            # inside of there pass in the title then pass in </h and the heading type and close it off

print(heading_generator('Greetings!', '1'))                 # then print out the heading generator with Greetings and 1 (h1 tag)
print(heading_generator('I am in a title', '3'))            # then print out the heading generator with I am in a title and 3 (h3 tag)
