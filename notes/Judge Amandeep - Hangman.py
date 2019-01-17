import random

List = ["Oh", "no!", "The", "goblins", "are", "coming", "to", "burn", "this", "village!"]
the_word = random.choice(List)
print(the_word)
list_of_letters = list(the_word)
print(list_of_letters)

guesses = 8
