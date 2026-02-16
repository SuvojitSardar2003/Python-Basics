class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

obj = Employee()
print(obj.a)  # Prints the a attribute
# print(o.b)  Shows an error as there is no b attribute in Employee class

obj = Programmer()

print(obj.a, obj.b)

obj = Manager()

print(obj.a, obj.b, obj.c)
