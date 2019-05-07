import csv


# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10
# (Modulo 10)


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS IS DIGITS")
    return False


def drop_last_digit(num: str):
    return num[:14]


def reverse_it(string):
    return string[::-1]


def multiply_it(num: str):
    last_num = int(num[15])
    new_num = reverse_it(drop_last_digit(num))
    num_list = list(new_num)
    sum = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            add = num_list[i]
            if add > 9:
                add -= 9
            sum += add
    if sum % 10 == last_num:
        return True
    return False


def validate_number(card_number):
    if not all_16_digits(card_number):
        return False
    if not multiply_it:
        return False
    return True


with open("Book1.csv", 'r') as old_csv:
            with open("MyNewFile.csv", 'w', newline='') as new_csv:
                print("Writing file... ")
                reader = csv.reader(old_csv)
                writer = csv.writer(new_csv)
                print("processing...")

                for row in reader:
                    old_number = (row[0])
                    last_num = int(old_number[0])
