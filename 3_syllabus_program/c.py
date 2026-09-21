# Write a program to find GCD of two numbers

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd_recursive(num1, num2)
print(f"GCD of {num1} and {num2} is: {result}")