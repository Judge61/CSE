import csv

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file... ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")
        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = int(row[0])
            first_num = int(old_number[0])
            if first_num % 2 == 0:
                writer.writerow(row)
            print(old_number)

print("OK")


with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", 'w', newline=' ') as new_csv:
        print("Writing file... ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]  # this is a string
            first_num = int(old_number[0])  # This is the first number....
            if first_num % 2 == 0:
                writer.writerow(row)
                # print(int(old_number) +1
                # print(old_number)

print("OK")