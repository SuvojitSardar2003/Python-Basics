# 6. WAP to find the factorial of a given number n using for loop.
n = int(input("Enter a number: "))
f = 1
if(n == 0):
    print(f"{n}!=1")
else:
    for i in range(1,n+1):
        f *= i
    print(f"{n}!={f}")