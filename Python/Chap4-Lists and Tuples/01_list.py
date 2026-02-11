# list is a mutable sequence of items, which means that you can modify the contents of a list after it has been created.
# Lists are defined using square brackets [] and can contain elements of different data types.
# Creating a list
my_list = [1, "Hello", 3.14, True]
# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: Hello
print(my_list[2])  # Output: 3.14
print(my_list[3])  # Output: True
# Modifying elements in a list
my_list[0] = 42
print(my_list)  # Output: [42, 'Hello', 3.14, True]
# Lists can also be created using the list() constructor
another_list = list([1, "World", 2.71, False])
print(another_list)  # Output: [1, 'World', 2.71, False]
# Lists can be nested, meaning that they can contain other lists as elements
nested_list = [1, [2, 3], "Nested"]
print(nested_list)  # Output: [1, [2, 3], 'Nested']
# Lists support various operations such as concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]
# Lists have built-in methods such as append(), extend(), insert(), remove(), pop(), and clear()
my_list.append("New Element")
print(my_list)  # Output: [42, 'Hello', 3.14, True, 'New Element']
my_list.extend([5, 6])
print(my_list)  # Output: [42, 'Hello', 3.14, True, 'New Element', 5, 6]
my_list.insert(1, "Inserted Element")
print(my_list)  # Output: [42, 'Inserted Element', 'Hello', 3.14, True, 'New Element', 5, 6]
my_list.remove(3.14)
print(my_list)  # Output: [42, 'Inserted Element', 'Hello', True, 'New Element', 5, 6]
popped_element = my_list.pop()
print(popped_element)  # Output: 6
print(my_list)  # Output: [42, 'Inserted Element', 'Hello', True, 'New Element', 5]
my_list.clear()
print(my_list)  # Output: []
# Lists can be unpacked into individual variables
a, b, c = list1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# Lists are often used to represent collections of items, such as a list of names or a list of numbers
names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5]
print(names)  # Output: ['Alice', 'Bob', 'Charlie']
print(numbers)  # Output: [1, 2, 3, 4, 5]
# Since lists are mutable, they cannot be used as keys in dictionaries or elements of sets
my_dict = {my_list: "This is a list as a key"}  # This will raise a TypeError because lists are unhashable
print(my_dict)
my_set = {my_list}  # This will also raise a TypeError because lists are unhashable
print(my_set)


friends = ["Apple","Orange",5,2.289,False,"Suvo","Raii"]

print(friends[0])

friends[0] = "Mango" #Unline Strings lists are mutable

print(friends[0])

print(friends[1:4])