
import csv

with open("Sales_Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        old_number = float(row[13])
        item_type = row[2]
        if item_type == "Fruits":
            total += float(row[13])
        if item_type == "Baby Food":
            total_1 += float(row[13])
        if item_type == "Beverages":
            total += float(row[13])
        if item_type == "Office Supplies":
            total += float(row[13])
        if item_type == "personal care":
            total += float(row[13])
        if item_type == "cereal":
            total += float(row[13])
        if item_type == "cosmetics":
            total += float(row[13])
        if item_type == "clothes":
            total += float(row[13])
        if item_type == "meat":
            total += float(row[13])
        if item_type == "snacks":
            total += float(row[13])
        if item_type == "vegetables":
            total += float(row[13])
        if item_type == "Household":
            total += float(row[13])

        # print(old_number)
    print(total)
               `
# Vegetables, beverages, office supplies, personal care, fruits, cereal, cosmetics, household, clothes, baby food, meat,
# snacks

#

# baby food: 863
# beverages- 864- 1715 851
#
# 1716- 2545 828
# 2546 - 3366 820
# 2547 - 4260 1713
# 4261 - 5111 850
# 5112 - 5940 828
# 5941 - 6783 842
# 6784- 7654  870
# 7655 - 8565 910
# 8566  - 9407 841
# 9408 - 10251 843




