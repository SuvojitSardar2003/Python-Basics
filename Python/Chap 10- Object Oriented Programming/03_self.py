# self refers to the instance of the class. It is automatically passed with a function call from an object.

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print(f"Good morning")

harry = Employee()
harry.language = "JavaScript" # This is an instance attribute

harry.getInfo()
harry.greet()
# Employee.getInfo(harry)

# Because Python methods are just functions inside a class.

# Unlike Java/C++, Python does NOT automatically bind the object unless you explicitly accept it as a parameter.

# self is a reference to the current instance of a class. It is automatically passed as the first argument to instance methods when a method is called through an object. It allows access to instance variables and other methods of the class.

#Is self a keyword in Python?

#Answer:
#No.
#It’s just a naming convention.

#def getInfo():

#TypeError: getInfo() takes 0 positional arguments but 1 was given

#Why is self not automatically added like in #Java?

#Answer:

#Because in Python, methods are just functions stored inside a class namespace. When accessed through an instance, Python binds the instance explicitly, so we must declare a parameter to receive it.