# 1. WAP using functions to find greatest of three numbers.
def greatest_of_three(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

result = greatest_of_three(num1, num2, num3)
print(f"Greatest among {num1}, {num2} and {num3} is : {result}") 