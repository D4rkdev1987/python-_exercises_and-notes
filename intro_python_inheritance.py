class User:                                           # create the class of user
  def __init__(self, email, first_name, last_name):   # function init with self email first name and last name passed in
    self.email = email                                # instance attributes for email first name and last name
    self.first_name = first_name                      
    self.last_name = last_name                         

  def greeting(self):                                 # function greeting and self
    return f'Hi {self.first_name} {self.last_name}'   # returns a formatted string here passed in first and last names
# is new element a new type of one of the classes you have already? if so because of admin yes
class AdminUser(User):                                # create the admin class here(inherits from User)to declare if one class inherits from another
  def active_users(self):                             # active users takes in self(class that inherits from class above)
    return '500'


tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens') # tiffany is an admin user, she has an email and first name and last name
 
kristine = User('kristine@devcamp.com', 'Kristine', 'Hudgens')   # and created a regular user here names kristine and the same attributes as above

print(tiffany.active_users()) # to have acess to the active users method 
print(tiffany.greeting())  # will print the full greeting because of inheritance-it works the child class has access to the attributes as the parent class and add on from there
print(kristine.active_users()) # if you try to have kristine access

# inheritance is the ability to create specialized classes