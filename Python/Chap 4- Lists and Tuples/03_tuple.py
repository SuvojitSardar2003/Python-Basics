# tuple is an immutable datatype, which means that once a tuple is created, its elements cannot be modified.
# Tuples are defined using parentheses () and can contain elements of different data types.
# Creating a tuple
my_tuple = (1, "Hello", 3.14, True)
# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello
print(my_tuple[2])  # Output: 3.14
print(my_tuple[3])  # Output: True
# Tuples can also be created without parentheses, using just commas
another_tuple = 1, "World", 2.71, False
print(another_tuple)  # Output: (1, 'World', 2.71, False)
# Tuples can be nested, meaning that they can contain other tuples as elements
nested_tuple = (1, (2, 3), "Nested")
print(nested_tuple)  # Output: (1, (2, 3), 'Nested')
# Tuples support various operations such as concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)
# Tuples have built-in methods such as count() and index()
print(tuple1.count(2))  # Output: 1
print(tuple1.index(2))  # Output: 1
# Tuples can be unpacked into individual variables
a, b, c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# Tuples are often used to represent fixed collections of items, such as coordinates or RGB color values
coordinates = (10, 20)
color = (255, 0, 0)
print(coordinates)  # Output: (10, 20)
print(color)  # Output: (255, 0, 0)
# Since tuples are immutable, they cannot be modified after creation, but they can be used as keys in dictionaries or elements of sets
my_dict = {my_tuple: "This is a tuple as a key"}
print(my_dict)  # Output: {(1, 'Hello', 3.14, True): 'This is a tuple as a key'}
my_set = {my_tuple, another_tuple}
print(my_set)  # Output: {(1, 'Hello', 3.14, True), (1, 'World', 2.71, False)}


t = (1,) # A tuple with a single element must include a comma to differentiate it from a regular parentheses expression
print(t) # Output: (1,)
print(type(t)) # Output: <class 'tuple'>
t2 = (1,45,342,2.289,True,"Suvo","Raii")
print(t2)