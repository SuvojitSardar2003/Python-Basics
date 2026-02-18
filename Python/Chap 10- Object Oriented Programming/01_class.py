# class is a blueprint for creating object

class Employee:
    language = "Java" # This is a class attribute
    salary = "1500000"

suvo = Employee()
suvo.name = "Suvojit" # This is an object or instance attribute
print(suvo.language, suvo.salary)

rohan = Employee()
rohan.name = "Rohan Roro"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class