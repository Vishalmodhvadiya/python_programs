# Write a program to implement an interactive calculator. User input is expected to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
# a. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# b. Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
# c. If the second input is not '+' or '-', again raise a FormulaError If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

class FormulaError(Exception):
    """Custom exception for invalid formula input."""
    pass


def evaluate_formula(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        raise FormulaError("Formula must consist of exactly 3 parts: number operator number")

    num1_str, operator, num2_str = parts

    try:
        num1 = float(num1_str)
    except ValueError:
        raise FormulaError(f"'{num1_str}' is not a valid number")

    try:
        num2 = float(num2_str)
    except ValueError:
        raise FormulaError(f"'{num2_str}' is not a valid number")

    if operator not in ('+', '-'):
        raise FormulaError(f"'{operator}' is not a valid operator (only '+' and '-' are supported)")

    if operator == '+':
        return num1 + num2
    else:
        return num1 - num2


print("Interactive Calculator (type 'quit' to exit)")

while True:
    user_input = input("\nEnter formula: ")

    if user_input.strip().lower() == "quit":
        print("Exiting calculator.")
        break

    try:
        result = evaluate_formula(user_input)
        print(f"Result: {result}")
    except FormulaError as e:
        print(f"Invalid formula: {e}")