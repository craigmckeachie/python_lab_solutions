import csv

with open('customers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile,)
    for row in reader:
        print(row['first_name'], row['last_name'])