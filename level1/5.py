def multiply(a,b):
    return a*b
    
a = int(input("enter number:"))

for b in range(1, 11):
    multiply(a,b)
    print("",a, "* ",b, "=" ,multiply(a,b))


