# Count Word Occurrences
def count_word(sentance, word):
    a = sentance.split()
    b = 0
    for i in a:
        if word == i:
            b += 1
    return b


sentance = input("enter sentance: ")
word = input("word: ")

count = count_word(sentance, word)
print(count)









# def count_word(sentance,word):
#     a = sentance.split()

# b = 0
# for i in a:
#     if word == i:
#        b += 1
#        print(b)

# sentance = input("enter sentance:")
# word = input("word:")

# count = count_word(sentance, word)
# print(count)

# count = count_word(sentance,word)
