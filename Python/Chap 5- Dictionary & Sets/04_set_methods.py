# Set methods in Python
my_set = {1, 2, 3, 4, 5}

# add() - Adds an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# remove() - Removes an element from the set (raises KeyError if element is not present)
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# discard() - Removes an element from the set if it is present (does not raise error if element is not present)
my_set.discard(7)  # No error raised
print(my_set)  # Output: {1, 2, 4, 5, 6}

# pop() - Removes and returns an arbitrary element from the set (raises KeyError if set is empty)
popped_element = my_set.pop()
print(popped_element)  # Output: An arbitrary element (e.g., 1)
print(my_set)  # Output: {2, 4, 5, 6}

# clear() - Removes all elements from the set
my_set.clear()
print(my_set)  # Output: set()

# copy() - Returns a shallow copy of the set
original_set = {10, 20, 30}
copied_set = original_set.copy()
print(copied_set)  # Output: {10, 20, 30}