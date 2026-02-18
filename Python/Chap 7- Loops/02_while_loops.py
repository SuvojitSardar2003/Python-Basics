# You can also use a while loop to achieve the same result:
i = 1
while i <= 5:
    print(i)
    i += 1
# Both of these loops will print the numbers from 1 to 5. The for loop is generally more concise and easier to read for this type of task, while the while loop can be more flexible for certain situations.

# Now let's see how we can use a while loop to iterate through a list:

list = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0
while(i<len(list)):
    print(list[i])
    i +=1