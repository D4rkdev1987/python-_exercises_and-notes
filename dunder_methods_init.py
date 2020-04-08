# double underscores-private and protected methods in classes__init__
# anytime you see the dunder it is a method given to you from python directly(don't override just USE IT)

class Invoice:                                # invoice class
    def __str__(self):                        # dunder string- pass in self(str method to help you get visabilty what you instatiated)
      return "This is the invoice class!"      
# python looks for str and looks for what is returned

inv = Invoice()                    # inv is instatiated for invoice
print(str(inv))                    # now print str and pass in the inv function
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

class Invoice:                                
  def __init__(self, client, total):          # dunder init takes in self and client and total
    self.client = client                      
    self.total = total                        

  def __str__(self):                                        # using string interpolation below
    return f"Invoice from {self.client} for {self.total}"   # pulling in the client and total


inv = Invoice('Google', 500)  # set inv to represent the invoice and passed in Google and 100 to show in the print statement
print(str(inv))               # calling the str method and calling the inv function