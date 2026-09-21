# Write a program to implement calculator.

def sum(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("enter your choise")
        print("1 for sum")
        print("2 for subtract")
        print("3 for multiplication")
        print("4 for division")
        print("5 for exit")

        choice = input("enter your choice : ")

        if choice == "5":
            print("exit calculator")
            break

        if choice not in ("1", "2", "3", "4"):
            print("invalid choice")
            break

        num1 = int(input("enter first number : "))
        num2 = int(input("enter second number : "))

        if choice == "1":
            print(f"Result: {sum(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")

calculator()