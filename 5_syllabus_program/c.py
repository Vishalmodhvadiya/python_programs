# Write a program to generate dictionary of frequency of alphabets of given string

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch, 0) + 1
    return freq


text = input("Enter a string: ")
result = char_frequency(text)
print("Character frequency:", result)