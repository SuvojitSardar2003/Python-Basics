print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):
    print(i)

# The range() function generates a sequence of numbers. In this case, it generates the numbers from 1 to 5 (the end number is exclusive).

# You can also use a while loop to achieve the same result:
i = 1
while i <= 5:
    print(i)
    i += 1
# Both of these loops will print the numbers from 1 to 5. The for loop is generally more concise and easier to read for this type of task, while the while loop can be more flexible for certain situations.

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)

