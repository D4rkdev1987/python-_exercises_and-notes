# ->>> allows you to process python code
# ->>> {name} is just calling the variable name
# ->>> f flag is format flag
# -----------------------------------------------------
# name = 'kristine'
# greeting = f'hi {name}'

# print(greeting)
#------------------------------------------------------
# heredocs
name = 'kristine'
product = 'Python elearning course'

email_content = f"""
hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""
print(email_content)
