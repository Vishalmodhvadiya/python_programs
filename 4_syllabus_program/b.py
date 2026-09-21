# Write a program to find frequency of elements of list

def frequency_of_elements(alist):
    frequency_dict = {}
    for item in alist:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

f = frequency_of_elements([1,2,3,2,4,1,5,3,6,4,4,3,2])
print(f)