#  Write a Python program that matches a string that has an a followed by one or more b's.

def match(string):
    i = 0
    while i < len(string):
        if string[i] == "a":
            j = i + 1
            count_b = 0
            while j < len(string) and string[j] == "b":
                count_b += 1
                j += 1
                if count_b >= 1:
                    return f"Match found: '{string[i:j]}'"
        i += 1
    return "no match found"


string = ["ab", "abbb", "a", "abc", "b", "xaybz", "aab"]


for s in string:
    print(f"{s}: {match(s)}")
