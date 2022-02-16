import csv

with open("bayareatemps.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Temp -Max"], row["Temp - Min"])