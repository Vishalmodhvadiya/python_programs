# Write a program that opens a file and writes data to it. Handle exceptions that can be generated during the I/O operations

from langsmith import expect

try:
    with open("7_syllabus_program/b.py", "w") as file:
        file.write("this is writing file b.py")
    print("File b.py created successfully.")

except FileNotFoundError:
    print("Error: The specified file path does not exist.")

except PermissionError:
    print("Error: You do not have permission to write to this file.")

except IsADirectoryError:
    print("Error: The given path is a directory, not a file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")