# Write a program to find minimum and maximum value in list of tuples.
# Write a program to remove an element from tuple.

def min_max_tuple(tuple_list):
    flat_list = []
    for tup in tuple_list:
        for value in tup:
            flat_list.append(value)

    for i in range(len(flat_list)):
        for j in range(i+1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                swap = flat_list[i]
                flat_list[i] = flat_list[j]
                flat_list[j] = swap

    return flat_list[0], flat_list[-1]

print(min_max_tuple([(1, 2), (3, 4), (0, 5), (6, 7)]))

def remove_element(tup, element):
    temp_list = []
    
    # Manually copy all elements except the one to remove
    for i in range(len(tup)):
        if tup[i] != element:
            temp_list.append(tup[i])
    
    return tuple(temp_list)

print(remove_element((10, 20, 30, 40, 50), 30))