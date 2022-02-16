import os

with open("users.txt", "r") as usersfile:
    for line in usersfile:
        os.makedirs("users/" + line.rstrip("\r\n"))