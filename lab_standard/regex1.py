import re
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
  print (match.group())  #Returns 'b@google' because we didn't account for hyphens or '.'s

match = re.search(r'[\w.-]+@[\w.-]+', str) # This will return the full email address because we are saying any alphanumeric character, . or hyphen can be in the string.
if match:
    print (match.group())