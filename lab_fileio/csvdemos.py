import csv
import json

csvReader = open("bayareatemps.csv", "r", encoding="utf-8-sig")
csvDictReader = csv.DictReader(csvReader)

for row in csvDictReader:
    print(row["Temp -Max"], row["Temp - Min"])

csvReader.seek(0)

jsonWriter = open("bayareatemps.json", "w")
output = json.dumps([row for row in csvDictReader ])
jsonWriter.write(output)

csvReader.close()
jsonWriter.close()
