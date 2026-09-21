# Write a program for matrix addition and matrix multiplication using list.

def matrix_addition(A, B):
    C = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    return C

def matrix_multiplication(A, B):
    C = []

    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum = sum + A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)

    return C


A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

X = [[1, 2, 3],
     [4, 5, 6]]

Y = [[7, 8],
     [9, 10],
     [11, 12]]


print("Matrix Addition:")
C = matrix_addition(A, B)

for row in C:
    print(row)


print("\nMatrix Multiplication:")
D = matrix_multiplication(X, Y)

for row in D:
    print(row)