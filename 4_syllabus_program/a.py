# Write a program to remove duplicates from list

def remove_duplicates(input_list):

    unique_list = []
    for item in input_list:
        if  item not in unique_list:
            unique_list.append(item)
    return unique_list

print(remove_duplicates([1, 2, 3, 2, 1, 4, 5, 3]))