class Html:                       # create a class called html
    def __init__(self, content):  #  create a function that brings in the init method and takes in self and content
        self.content = content    #  stores content in a instance vraible here

    def render(self):              # abstract function called render and self passed in
        raise NotImplementedError("Subclass must implement render method")    # raise notImplementedError-have to access function or won't work


class Heading(Html):                       # create a child class called heading inherits from the Html class
    def render(self):                      # calls in the render fucntion
        return f'<h1>{self.content}</h1>'  # 


class Div(Html):                           # class takes in the Html class
    def render(self):                        # has it's own render method that takes in self
        return f'<div>{self.content}</div>'  # 


tags = [Div('Some content'), Heading('My Amazing Heading'), Div('Another div')]    #
# above-create a list called tags and add elements-call Div class and pass in content
#then heading element and pass in content
# and then Div 
for tag in tags:                               # iterate through the list
    print(str(tag) + ': ' + tag.render())      # debugging purpose print out the string value(tag-string representation) concat a colon and call the render function
    print(tag.render())                        # rendered your own HTML here, created an abstract class, with child class and it printed

# poly means many and morphism is change so basically many changes -Polymorphism    