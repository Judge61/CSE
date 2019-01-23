from random import choice

word = choice(["cool", "hello", "testing", "goblins", "are", "coming", "to", "burn", "this", "village"])

guessed = []
wrong = []

guesses = 8
win = False
while guesses > 0 and not win:

    random = ""
    for letter in word:
        if letter in guessed:
            random = random + letter
        else:
            random = random + "*"

    if random == word:
        print("You Win!")
        win = True
        continue

    print("Guess the word:", random)
    print(guesses, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        guesses = guesses - 1
        wrong.append(guesses)

    print()

if guesses:
    print("You guessed", word)
else:
    print("You didn't get", word)
