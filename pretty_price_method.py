# function if its passed in a gross value
# 3.21
# 3.99 we want this
# pretty_price(3.20, 0.99) out put should be > 3.99
# int returns the integer value so 3.23 will return 3 it strips it

def pretty_price(gross_price, extension):  # create a funciotn called pretty price and takes 2 arguments what the sale price is and then the decimal extension
    if isinstance(extension, int):         #conditional check if extension of interger- say if isinstance(function)-instance of integer
        extension = extension * 0.01       # reassign etentsion is equal to extension times 0.01
    return int(gross_price) + extension    #convert gross price-return int gross price and add to the extension

print(pretty_price(3.50, 0.95))    
print(pretty_price(3.50, 95))   