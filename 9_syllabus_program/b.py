# Write a Python program to find sequences of lowercase letters joined with a underscore.

def find_lowercase_letters(string):
    lowercase_letters = []
    for char in string:
        if char.islower():
            lowercase_letters.append(char)
    return lowercase_letters

s = find_lowercase_letters("Hello World! This is a Test String.")
joined_string = '_'.join(s)
print(s)
print(joined_string)
