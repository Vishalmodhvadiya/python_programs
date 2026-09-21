# Write a Python program to sum all the items in a dictionary

def sum_dict_values(d):
    total = sum(d.values())
    return total


data = {"a": 10, "b": 20, "c": 30}
result = sum_dict_values(data)
print("Dictionary:", data)
print("Sum of values:", result)