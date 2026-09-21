# Write a program that calculates division of two vectors and returns the result vector

def division_of_vectors(v1, v2):
    v3 = []
    if len(v1) != len(v2):
        raise ValueError("vectors must be of the same length")

    for i in range(len(v1)):
        try:
            division = v1[i] / v2[i]
            v3.append(division)
        except ZeroDivisionError:
            print(f"division by zero at index {i} is not possible ")
            v3.append(None)   

    return v3


D = division_of_vectors([10, 20, 30, 60, 25], [2, 4, 4, 5, 0])
print(D)
