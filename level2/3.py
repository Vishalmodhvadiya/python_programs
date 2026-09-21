# Print Only Odd Numbers from a List
mylist = []
for i in range(8):
    num = int(input("enter number="))
    mylist.append(num)
print(mylist)
odd_list = []
for i in range(8):
    value = mylist[i]
    if value % 2 != 0:
     odd_list.append(value)
print(odd_list)
