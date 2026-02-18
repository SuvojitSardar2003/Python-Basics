# 3. A list contains the multiplication table of 7, WAP to convert it to vertical string of same numbers.

table = [str(7*i) for i in range(1,11)]
# print(table)

s = "\n".join(table)
print(s)