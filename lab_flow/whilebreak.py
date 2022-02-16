import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
attempts = 0

while True:
    if not EMAIL_REGEX.match(input('Test if email is valid: ')):
        attempts = attempts + 1
        if attempts <= 3:
            print("Email is not valid, try again")
        else:
            print("You can't try more than 3 times.")
            break
    else:
        print("Valid Email")
        break