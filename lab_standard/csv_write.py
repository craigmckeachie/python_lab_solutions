import csv

with open('customers.csv', 'w', newline='') as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=',')
    csvWriter.writerow(['first_name', 'last_name', 'email_address'])
    csvWriter.writerow(['Fred', 'Flintstone', 'fflintstone@bedrock.com'])
    csvWriter.writerow(['Wilma', 'Flintstone', 'wflintstone@bedrock.com'])
    csvWriter.writerow(['Barney', 'Rubble', 'brubble@bedrock.com'])
    csvWriter.writerow(['Betty', 'Rubble', 'berubble@bedrock.com'])