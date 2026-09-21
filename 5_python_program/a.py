# Write a program to map 2 lists into a dictionary.

def map_lists_to_dict(keys, values):
    result = dict(zip(keys, values))
    return result


keys = ["name", "age", "city"]
values = ["Alice", 25, "Delhi"]

result = map_lists_to_dict(keys, values)
print("Mapped dictionary:", result)