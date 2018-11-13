number = 5
guesses = 5
win = False

while guesses > 0:
    num = int(input("What's a number from 1-10"))
    if num > 11:
        print("Way too high ")
        guesses = guesses - 1
    elif num > number:
        print("The number is lower")
        guesses = guesses - 1
    elif num < number:
        print("The number is higher")
        guesses = guesses - 1
    elif num == number:
        print("congratulations!!!!")
        guesses = 0
alt1