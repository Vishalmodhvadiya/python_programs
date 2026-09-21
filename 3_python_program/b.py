# Write a program which takes a sentence from user and calculates number of digits, letters, uppercase letters, lowercase letter and spaces in sentence.

def calculate_word(sentence):
  
    digits = 0
    letters = 0
    uppercase = 0
    lowercase = 0
    spaces = 0

    for ch in sentence:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            letters += 1
            if ch.isupper():
                uppercase += 1
            elif ch.islower():
                lowercase += 1
        elif ch.isspace():
            spaces += 1

    return digits, letters, uppercase, lowercase, spaces


sentence = input("enter a sentance:")
digits, letters, uppercase, lowercase, spaces = calculate_word(sentence)

print(f"\nDigits: {digits}")
print(f"Letters: {letters}")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Spaces: {spaces}")
