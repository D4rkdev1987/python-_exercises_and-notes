# ->>> allows you to process python code inside of strings
# ->>> {name} is just calling the variable name--anything in curly brackets will be ran as python script
# ->>> f flag is format flag
# ---------------------------------------------------------
name = 'kristine'   #variable is name and string is kristine
greeting = f'hi {name}'    

print(greeting)
#----------------------------------------------------------

# heredoc
name = 'kristine'      #variable name
product = 'Python elearning course'  #variable product
# below is set to a heredoc with the """ after the format flag (f)
email_content = f"""  
hi {name} 

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(email_content)
