import csv

with open("customers.csv", mode= "r") as customers_csv_file:
    csv_reader = csv.DictReader(customers_csv_file)
    with open("customer_emails.txt", "w") as customers_email_file:
        for row in csv_reader:
            email = row["email_address"]
            print(email)
            customers_email_file.write(email + "\n")