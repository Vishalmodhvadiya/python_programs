# task: Take a sentence as input from the user and print each word on a separate line with its word number.
sentance = input("enter sentance=")
a = sentance.split()
print(a)
n = 1;
for  i in a:
    print(" ",n, i)
    n= n + 1

