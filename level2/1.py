 #Largest and Smallest in a List
mylist = []
for i in range(5):
    num = int(input("enter number:"))
    mylist.append(num)
print(mylist)
smallest = min(mylist)
largest = max(mylist)
print("smallest number",smallest)
print("largest number",largest)

