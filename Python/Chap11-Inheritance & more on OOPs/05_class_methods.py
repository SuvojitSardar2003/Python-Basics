# A class method is a method which is bound to the class and not the object of the class @classmethod decorate is used to create a class method

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()

# @classmethod receives cls, which refers to the class, not the object.
# 
# So cls.a → accesses Employee.a
# 
# It ignores instance attribute e.a

#If interviewer asks:

#Why does it print 1 instead of 45?

#Because @classmethod receives the class as the first argument (cls), so cls.a accesses the class attribute. Instance attributes are not considered when accessing via cls.

Employee.a = 100
e.show()
# The class attribute of a is 100