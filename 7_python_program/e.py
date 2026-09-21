# Write a program to find reciprocal of the elements of list [12,0,‟a‟,20,‟hi‟] with Exception handling.

def find_resippocal(list):
    resipocal_list = []
    for item in list:
        try:
            resipocal = 1/item
            resipocal_list.append(resipocal)
            print(f"resipocal of {item} is {resipocal}")
        except ZeroDivisionError:
           print("error: division by zero is not valid")
        except TypeError:
           print("error: invalid type, enter numbers only")

    return resipocal_list
 
data =  [12,0, "a",20, "hi"]
result = find_resippocal(data)
print(result)


