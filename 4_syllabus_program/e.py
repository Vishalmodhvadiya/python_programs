# Write a program to generate Pascal’s triangle using list.

def generate_pascals_triangle(num_rows):
    triangle = []
    row = []

    for i in range(num_rows):
        # Insert 1 at the start, then add adjacent pairs, end with 1
        row.insert(0, 1)
        for j in range(1, len(row) - 1):
            row[j] = row[j] + row[j + 1]
        triangle.append(row.copy())

    return triangle


def print_pascals_triangle(triangle):
    num_rows = len(triangle)
    for i, row in enumerate(triangle):
        print(" " * (num_rows - i), end="")
        print(" ".join(map(str, row)))


n = int(input("Enter number of rows: "))
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)