import random
import string

List = ["Oh", "no!", "The", "goblins", "are", "coming", "to", "burn", "this", "village!"]
the_word = random.choice(List)
print(the_word)
list_of_letters = list(the_word)
print(list_of_letters)

print(list(string.ascii_letters))
print(list(string.digits))
print(list(string.punctuation))

oh = "black"
no = "black"
The = "black"
are = "black"
coming = "black"
to = "black"
village = "black"
burn = "black"
goblins = "black"
this = "black"
