# Write a script to concatenate given dictionaries

def concatenate_dicts(dict1, dict2):
    merged = {**dict1, **dict2}
    return merged

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

result = concatenate_dicts(d1, d2)
print("Dict 1:", d1)
print("Dict 2:", d2)
print("Merged:", result)