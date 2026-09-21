# Write a program to sort given list.

def sort_list(input_list):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] > input_list[j]:
                swap = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = swap
    return input_list

print(sort_list([5, 2, 9, 1, 6]))