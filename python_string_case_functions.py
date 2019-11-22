# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper() 

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower())



"""
str.upper()
Return a copy of the string with all the cased characters [4] converted to uppercase. Note that s.upper().isupper() might be False > if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. > “Lt” (Letter, titlecase).

str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase.
"""