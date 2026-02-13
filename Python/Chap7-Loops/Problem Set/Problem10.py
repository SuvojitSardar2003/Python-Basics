# 10. WAP to print multiplication table of a given number n in reverse order using for loop.

n = int(input("Enter a number: "))

# for i in range(start,stop,step)
for i in range(10,0,-1):
    print(f"{n} x {i} = {n*i}")

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")