# 2. WAP to input eight numbers from user and display all the unique numbers in a set.
unique_numbers = set()
for i in range(8):
    num = int(input("Enter a number: "))
    unique_numbers.add(num)
print("Unique numbers:", unique_numbers)