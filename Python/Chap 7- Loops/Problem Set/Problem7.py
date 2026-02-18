# 7. WAP to print the following star patters.
#   *
#  ***
# *****   for n = 3

n = int(input("Enter a number: "))
#for i in range(1, n+1):
#    for j in range(1, n-i+1):
#        print(" ", end="")
#    for k in range(1, 2*i):
#        print("*", end="")
#    print()

for i in range(1, n+1):
    print(" "*(n-i),end="")
    print("*"*((2*i)-1),end="")
    print()