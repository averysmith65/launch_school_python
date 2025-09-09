# Starting with the string:

munsters_description = "The Munsters are creepy and spooky."

# print the string with the case of all letters swapped:
# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

swapped = ""

for char in munsters_description:
    if char.isupper():
        swapped += char.lower()
    else:
        swapped += char.upper()

print(swapped)