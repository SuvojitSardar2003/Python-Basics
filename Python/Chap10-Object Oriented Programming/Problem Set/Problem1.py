# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

suvo = Programmer("Suvojit","Java","1500000")
print(suvo.name, suvo.language, suvo.salary)

tanmoy = Programmer("Tanmoy", "Python", "120000")
print(tanmoy.name, tanmoy.salary, tanmoy.language)