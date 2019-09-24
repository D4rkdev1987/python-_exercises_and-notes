"""
#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the
#number and for the multiples of five print “Buzz”. For
#numbers which are multiples of both three and five print
“FizzBuzz”.
-functions
-looping
-conditionals
-math operators 

first create the function with a arbitrary max
loop through entire set of numbers for in loop
for num in range starting at 1 going to max num plus 1 (plus 1 to go to 100
from there implement the conditional)
now to check for the items (3 conditionals)
if the number modulo 3 and zero and num modulo 5 and equal to 0 print Fizzbuzz
else if if it just simply divisiable by 3 print fizz
lastly and if it divisable by 5 just print buzz (3rd condition
else print number itself (num))
"""

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)