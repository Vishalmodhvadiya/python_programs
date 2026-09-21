# Common Elements in Two Lists
def get_value():
    value = []
    for i in range(4):
      a = int(input("enter a1:"))
      value.append(a)
    return(value)
def get_num():
    num = []
    for i in range(4):
     b = int(input("enter b1:"))
     num.append(b)
    return(num)
def find_comman(value, num):
    comman = []
    for v in value:
     for n in num:
      if v == n:
        comman.append(v)
    return (comman)
value = get_value()
num = get_num()

result = find_comman(value, num)
print(result)
