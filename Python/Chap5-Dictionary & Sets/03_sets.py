# Set is a collective data type that is unordered, mutable, and does not allow duplicate elements.
# Sets are defined using curly braces {} or the set() constructor.

#Empty set
empty_set = set()
print(empty_set)  # Output: set()
# Don't use empty curly braces {} to create an empty set, as it creates an empty dictionary instead.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
another_set = set([3, 4, 5, 6, 7])
print(another_set)  # Output: {3, 4, 5, 6, 7}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Checking for membership
print(4 in my_set)  # Output: True
print(3 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Set comprehension
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # Output: {1, 4, 9, 16, 25}

# Frozen set (immutable set)
frozen_set = frozenset([1, 2, 3])
print(frozen_set)  # Output: frozenset({1, 2, 3})