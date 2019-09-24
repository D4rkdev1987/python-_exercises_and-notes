# function if its passed in a gross value
# 3.21
# 3.99 we want this
# pretty_price(3.20, 0.99) out put should be > 3.99

def pretty_price(gross_price, extension):
    if isinstance(extension, int):#conditional check if extension of interger
        extension = extension * 0.01 
    return int(gross_price) + extension #convert gross price

print(pretty_price(3.50, 0.95))    
print(pretty_price(3.50, 95))   