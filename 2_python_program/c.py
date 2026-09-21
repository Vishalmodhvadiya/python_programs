# Write a program to swap the values of two variables without using temporary variable.

def swap(a,b):

    print("value of a before swaping :",a)
    print("value of b before swaping :",b)
    a = a + b
    b = a - b
    a = a - b
    print("value of a after swap: ",a)
    print("value of b after swap: ",b)

swap(5,7)