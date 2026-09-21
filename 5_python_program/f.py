# Create a dictionary where keys are name of students and values are another dictionary containing semester, age and cpi of that student.
# ● Print all the names of students.
# ● Print only names of students

students = {
    "Alice": {"semester": 5, "age": 20, "cpi": 8.9},
    "Bob": {"semester": 3, "age": 19, "cpi": 7.5},
    "Charlie": {"semester": 6, "age": 21, "cpi": 9.1}
}


print("All student names:")
for name in students:
    print(name)

print("\nNames as a list:")
names_list = list(students.keys())
print(names_list)