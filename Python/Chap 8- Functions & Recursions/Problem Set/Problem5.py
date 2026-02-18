# 5. Write a python function to print first n lines of the following pattern using recursion:
# * * *
# * *
# *  for n =3

def print_pattern(n):
    if(n <= 0):
        return
    else:
        print("* "*n)
        print_pattern(n-1)

n = int(input("Enter a positive number: "))
print_pattern(n)