class Website:                         #
    def __init__(self, title):         # function init that takes in self and the title of the website
      self.title = title               # self.title set equal to what ever the title is passed in

#instance attribute-belongs to this specific instance
#they are data values specific for the instance
ws = Website('My Website Title')      # set ws as the Website
print(ws.__dict__)                    # __dict__ -returns the attributes and their values in dictionary form
                                      # # returns {'title': 'My Website Title'}
#another instance-you would need to pass in another value
ws_two = Website('My Second Title')   # this will print out the second title
print(ws_two.__dict__)                # returns {'title': 'My Second Title'}
#---------------------------------------------------------------------------------------------------------------
#class attribute-title below is hard coded in 
class DifferentWebsite:               # create the class DifferentWebsite
  title = 'My Class Title'            # passin a variable here title is equal to my class title

dw = DifferentWebsite()               # create the instance of the class-dw is equal to DifferentWebsite
print(dw.title)                       # simply call dw.title to return the value(not treated the same) (__dict__ won't return a dictionary)

dw_two = DifferentWebsite()      
print(dw_two.title)

# differences class attritubute belongs to class definition and called any time you need it, hard coded into class (similar to having a function in the class and having access to it)
# instance belongs to the instance-for every other instance you must pass in a different instance