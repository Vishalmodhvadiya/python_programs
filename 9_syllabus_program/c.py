# Write a Python program to find all five characters long word in a string

def five_letter(text):
    words = text.split()
    words_list = []

    for word in words:
        cleaned_word = ''.join(ch for ch in word if ch.isalnum())
        if len(cleaned_word) == 5:
            words_list.append(cleaned_word)

    return words_list


sentence = "Hello is done world these words apple happy about class extra ok bat"
result = five_letter(sentence)
print("Five letter words:", result)