# Write a program for find factorial of a given number using iterative and recursive function.


# iterative function.

def fact_iterative(n):

    if n < 0:
        raise ValueError ("number is negative")
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(1, n+1):
         result *= i
    return result

#recursive function.

def fact_recursive(n):

    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact_recursive(n -1)


n = int(input("enter number : "))
print(fact_iterative(n))
print(fact_recursive(n))