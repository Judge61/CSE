import random
print(random.randint(0, 10))
playing = True
guesses_left = 5
while guesses_left > 0 and playing:
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"