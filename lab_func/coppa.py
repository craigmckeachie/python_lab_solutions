"""
Checks the birthday for COPPA compliance
"""
import datetime

TEMP_TODAY = datetime.datetime.now()

def check_birthday(year, month, day):
    """
    Takes a year, month, and day to check if user is at least 13 years old.
    """
    if (year + 13, month, day) > (TEMP_TODAY.year, TEMP_TODAY.month, TEMP_TODAY.day):
        print("Must be at least 13 years old according to COPPA regulations")
        return False
    return True