
import csv

with open("Sales_Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    total_babyfood= 0
    total_beverages = 0
    total_meat = 0
    total_personal = 0
    total_household = 0
    total_officesupplies = 0
    total_cosmetics = 0
    total_cereal = 0
    total_snacks = 0
    total_clothes = 0
    total_vegetables = 0

    for row in reader:
        if row[0] == 'Region':
            continue
        old_number = float(row[13])
        item_type = row[2]
        if item_type == "Fruits":
            total += float(row[13])
        if item_type == "Baby Food":
            total_babyfood += float(row[13])
        if item_type == "Beverages":
            total_beverages += float(row[13])
        if item_type == "Office Supplies":
            total_officesupplies += float(row[13])
        if item_type == "Personal Care":
            total_personal += float(row[13])
        if item_type == "Cereal":
            total_cereal += float(row[13])
        if item_type == "Cosmetics":
            total_cosmetics += float(row[13])
        if item_type == "clothes":
            total_clothes += float(row[13])
        if item_type == "meat":
            total_meat += float(row[13])
        if item_type == "Snacks":
            total_snacks += float(row[13])
        if item_type == "Vegetables":
            total_vegetables += float(row[13])
        if item_type == "Household":
            total_household += float(row[13])

        # print(old_number)
    print(total_snacks)

profits = ["total", "total_babyfood", "total_beverages", "total_meat", "total_personal", "total_household",
"total_officesupplies","total_cosmetics", "total_cereal", "total_snacks", "total_clothes", "total_vegetables"]
if max(profits) == total:
    print("Fruits is the most profitable")
if max(profits) == total_vegetables:
    print("Vegetables is the most profitable")
if max(profits) == total_household:
    print("Household is the most profitable")
if max(profits) == total_clothes:
    print("Clothes  is the most profitable")
if max(profits) == total_cosmetics:
    print("Cosmetics is the most profitable")
if max(profits) == total_cereal:
    print("Cereal is the most profitable")
if max(profits) == total_meat:
    print("Meat is the most profitable")
if max(profits) == total_beverages:
    print("Beverages is the most profitable")
if max(profits) == total_personal:
    print("Personal Care is the most profitable")
if max(profits) == total_officesupplies:
    print("Office Supplies is the most profitable")
if max(profits) == total_babyfood:
    print("Baby Food is the most profitable")
if max(profits) == total_snacks:
    print("Snacks is the most profitable")
# Vegetables, beverages, office supplies, personal care, fruits, cereal, cosmetics, household, clothes, baby food, meat,
# snacks




