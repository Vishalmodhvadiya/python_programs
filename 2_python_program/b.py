#  Write a program to find the maximum number out of 3 numbers.

def max_number(a,b,c):
    if a > b and a > c:
        print("maximum_number :",a)
    elif b > a and b > c:
        print("maximum_number :",b)
    else:
        print("maximum_number :",c)

max_number(7,9,5)