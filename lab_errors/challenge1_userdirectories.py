"""
File based subdir creation. This program accepts a filename on the command line and
creates a subdirectory named for each line in the file under ./users
"""

import os
import sys

PATH = "users/"

try:
    assert len(sys.argv) == 2, "You must pass a single user list file on the command line"
    with open(sys.argv[1], "r") as usersfile:
        for line in usersfile:
             os.makedirs(PATH + line.rstrip("\r\n"))
except FileExistsError as err:
    print("Directory already exists: ", err)
except FileNotFoundError as notFoundError:
    print("Directory doesn't exist: ", notFoundError)
except:
    print("Unexpected error: ", sys.exc_info())
else:
    print("Program exiting normally")
finally:
    print(PATH)
    files = os.listdir(PATH)
    for f in files:
        print(f)