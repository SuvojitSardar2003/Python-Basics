# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter a number: "))

list = [n*i for i in range(1,11)]
print(list)

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt
with open("Tables.txt","a") as f:
    f.write(f"Table of {n}: {str(list)}\n")