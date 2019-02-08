import string

print(list(string.ascii_letters))
print(list(string.digits))
print(list(string.punctuation))


# It is not Arizona
states["AR"] = "Arizona?"
# Fixed it
states['AR'] = "Arkansas"
print(states['AR'])
