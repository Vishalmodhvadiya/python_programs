#  Declare a class Person having name as member. Derive two classes 
# a. Businessman - having income and number of people involved in his business as members.
# b. Employee - having income as a member.
# c. Create objects of both the classes and compare the income and print the  name of one having greater income.


class Person:
    def __init__(self, name):
        self.name = name

class Business(Person):
    def __init__(self, name, income, number_of_people):
        super().__init__(name)
        self.income = income
        self.number_of_people = number_of_people

class Employee(Person):
    def __init__(self, name, income):
        super().__init__(name)
        self.income = income

b = Business("vishal", 5000, 10)
e = Employee("parth", 30000)


if b.income > e.income:
    print(b.name)
elif e.income > b.income:
    print(e.name)
else:
    print("Both have equal income")
