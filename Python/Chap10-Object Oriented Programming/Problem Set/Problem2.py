# 2. Write a class "calculator" capable of finding square,cube and square root of a number.

class calculator:
    def __init__(self,n):
        self.n = n
    
    @staticmethod
    def greet():
        print("Hello there!")
    
    def square(self):
        print(f"The square is : {self.n * self.n}")
    
    def cube(self):
        print(f"The cube is : {self.n * self.n * self.n}")
    
    def squareRoot(self):
        print(f"The square-root is : {self.n ** 1/2}")

a = calculator(4)
a.greet()
a.square()
a.cube()
a.squareRoot()

# 4. Add a static method in problem 2, to greet the user with hello.