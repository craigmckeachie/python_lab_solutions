"""
Registers users, checking for COPPA compliance
"""
import coppa

def registration(dobstatus):
    """
    Takes a boolean and prints if the resulting birthday is valid or not.
    """
    if dobstatus is True:
        print("Valid Birthday")
    else:
        print("Invalid DOB, must be at least 13 years old according to COPPA regulations")

if __name__ == "__main__":
    YEAR = int(input('Enter year of birth YYYY: '))
    MONTH = int(input('Enter month of birth MM: '))
    DAY = int(input('Enter day of birth DD: '))
    registration(coppa.check_birthday(YEAR, MONTH, DAY))