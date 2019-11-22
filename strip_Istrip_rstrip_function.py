url = 'https://google.com'
print(url.strip('https://')) # to take off the https:// in the link make sure to pass it in as a string

url = url.lstrip('https://') # this is called left strip-starts on the left and goes to the exact match
url = url.rstrip('.com') # this is right strip-goes to the string and starts from end and moves to the left
print(url.capitalize()) #capitalize will print Google with the G capitalized

