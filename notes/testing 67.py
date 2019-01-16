from random import choice

word = choice(["Oh", "no!", "The", "goblins", "are", "coming", "to", "burn", "this", "village!"])

guessed = []
wrong = []

guesses = 8

while guesses > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess the word:", out)
    print(guesses, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = guesses - 1
        wrong.append(guess)

    print()

if guesses:
    print("You guessed", word)
else:
    print("You didn't get", word)
