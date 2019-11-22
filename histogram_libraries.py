"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    # 4 different elements(data points) -(sales data)
t $$$$$$$$$$
o $$$$$$$$$$$$
"""
#type of chart in statistics for patterns and see trends of data

#then each element rep. sale count
# utitlize 4 * 'w'

sales = {        #created a dictionary called sales
  'google': 20,
  'facebook': 42,   #all key value pairs based dictionary
  'twitter': 10,
  'offline': 12,
}

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')