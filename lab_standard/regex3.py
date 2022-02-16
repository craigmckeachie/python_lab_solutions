import re

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'([\w\.-]+)@[\w\.-]+', str) # Simply put parentheses around the portion we want to extract out - the subgroup
for email in emails:
    print (email)