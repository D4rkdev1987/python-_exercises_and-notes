sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'Dog'  # variable word set to dog

if word.lower() in sentence.lower():  # if lower function in the sentence (lower function) TAKE ALL VALUES AND LOWER CASE IT HERE
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')
#--------------------------------------------
#--------------------------------------------

nums = [1, 2, 3, 4]  # a list of numbers

if 3 in nums:        # if 3 is in nums list
  print('The number was found') # print The number was found
else:                 # if not
  print('The number was not found') # print the number was not found