# 1. WAP to find the greatest of four numbers entered by the user.

list = []
for i in range(4):
    num = int(input("Enter a number: "))
    list.append(num)
greatest = max(list)
print("The greatest number is: ", greatest)

#using conditional expression
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("The greatest number is: ", a)
elif(b>a and b>c and b>d):
    print("The greatest number is: ", b)
elif(c>a and c>b and c>d):
    print("The greatest number is: ", c)
else:
    print("The greatest number is: ", d)