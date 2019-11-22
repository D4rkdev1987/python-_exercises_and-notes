sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('quick')
query_two = sentence.index('oops')

print(query)
print(query_two)

query = 'oops' in sentence

print(query)

# to search in a string
# start with the variable sentence with a string with a sentence
# start with a query you first call the senetence then in parens type quick-which will return the index where quick is (this a a substring)
# NEXT
# the index function returns the similar finding of using find-BUT index will throw and error if it can't find
# if value is not contained in the string INDEX will throw an error while FIND will show an -1
#NEXT
# for the in operator- pass in the fox word to start which will display TRUE if you pass in oops it will return FALSE

















