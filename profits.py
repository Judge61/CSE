import csv

with open("Sales_Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        old_number = (row[2])
        print(old_number)
# Vegetables, beverages, office supplies, personal care, fruits, cereal, cosmetics, household, clothes, baby food, meat,
# snack
