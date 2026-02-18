# 5. WAP which finds out whether a given name is present in a list or not.

list = ["Suvojit", "Shyamoshree", "Suvo", "Raii", "Arjo"]

name = input("Enter a name: ")

if(name in list):
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")