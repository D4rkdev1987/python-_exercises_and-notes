# Guide to the sorted Function in Python

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]
#sale_prices.sort()
#sort sorts all elements in place
#sorted has same type of behavior but allows you to store inside of a variable

sorted_list = sorted(sale_prices, reverse=True) # pass sale_prices passed in as an argument- and then here we used reverse as another optional argument

print(sorted_list)
