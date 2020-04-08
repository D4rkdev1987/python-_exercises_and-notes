# import a custom library inside the python repl
import math                  # pulling in the math library say import math then press return
math.sqrt(4)                 # you can say math square root and pass in any number in the parens


# Place in file create_custom_module_import
def greeting(first, last):     # create the function and pass in the first and last as arguments
  return f'Hi {first} {last}!' # now return the values 
#-----------------------------------------------------------------------------
# Call from repl start the python environment
import helper                    # name is create_custom_module_import NOT helper

helper.greeting('Kristine', 'Hudgens')  # 