# Write a program that prompts the user to enter a number. If the number is positive or zero print it, otherwise raise an exception. A message “Code execution completed” should be displayed in both the cases, at the end of the execution.


def check_number(user_input):
    if user_input >= 0:
        print(user_input)
    else:
        raise ValueError("Error: The input is negative. Please provide a positive number or zero.")

try:
    num = int(input("Enter a number: "))
    check_number(num)
except ValueError as e:
    print(e)
finally:
    print("Code execution completed")