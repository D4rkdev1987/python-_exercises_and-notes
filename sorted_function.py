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
#sort sorts all elements in place
#sorted has same type of behavior but allows you to store inside of a variable

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)
