class Heading:                        # heading class
    def __init__(self, content):      
      self.content = content          

    def render(self):                      
      return f'<h1>{self.content}</h1>'    

class Div:                              # div class
  def __init__(self, content):          
    self.content = content              

  def render(self):                        
    return f'<div>{self.content}</div>'    

div_one = Div('Some content')              # stored in variables
heading = Heading('My Amazing Heading')    
div_two = Div('Another div')                
                                           # behavior is identical-use below if don't have a lot of shared behavior but call the same function
def html_render(tag_object):               #  create the function html_render it takes in the tag object anything that has a render function
  print(tag_object.render())               # print the tag object(calling render function)

html_render(div_one)   
html_render(div_two)
html_render(heading)