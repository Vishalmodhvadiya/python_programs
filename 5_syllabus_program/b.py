# Write a program to invert keys and values of dictionary

def invert_dict(d):
    inverted = {value: key for key, value in d.items()}
    return inverted


original = {"a": 1, "b": 2, "c": 3}
result = invert_dict(original)
print("Original:", original)
print("Inverted:", result)