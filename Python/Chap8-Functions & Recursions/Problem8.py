# 8. Write a python function to print multiplication table of a given number n.
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
n = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(n)