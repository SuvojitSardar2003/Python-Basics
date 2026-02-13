# 1. WAP to print multiplication table of a given number n using for loop.

n = int(input("Enter a number: "))
i=1
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")