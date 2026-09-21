# Write a program to read n integers from the keyboard and store them into a file total.txt file, separate odd and even numbers and store them in odd.txt and even.txt file. Display the content of all three files.
def numbers_files():
    n = int(input("Enter a number: "))
    numbers = []

    for i in range(n):
        num = (int(input(f"enter number {i + 1}: ")))
        numbers.append(num)

    try:
        with open("total.txt", "w") as total_file:
            for num in numbers:
                total_file.write(f"{num}\n")

        with open("even.txt", "w") as even_file:
            for num in numbers:
                if num % 2 == 0:
                    even_file.write(f"{num}\n")

        with open("odd.txt", "w") as odd_file:
            for num in numbers:
                if num % 2 != 0:
                    odd_file.write(f"{num}\n")

    except IOError as e:
        print(f"error occured while writing file{e}")

def display_files(filename):
    try:
          with open(filename, "r") as file:
             file.read()

    except FileNotFoundError:
        print("files not found.")


numbers_files()
display_files("total.txt")
display_files("even.txt")
display_files("odd.txt")
