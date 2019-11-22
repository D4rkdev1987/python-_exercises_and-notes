# The quick brown fox jumped
# T => 0    every first element has an index of zero to start
# h => 1
# e => 2
# ' ' => 3   the space is index of three-python counts spaces as well

starter_sentence = 'The quick brown fox jumped'
#in brackets you pass in what ever index you want to use [ ]
#emutability means you can't change an element-can't alter the string once it's created
#RANGES
#to be brought the T [0:3] would start at 0 and go to the 3rd index number-in this case it will end at 3rd index and show The
new_sentence = 'Thy' + starter_sentence[3:] #to change-start with saying Thy then pull in the starter 

print(new_sentence)



