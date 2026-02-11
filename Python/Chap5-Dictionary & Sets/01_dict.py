# Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed and can not have duplicate keys.
# Dictionaries are written with curly brackets, and they have keys and values.

# Create a dictionary
my_dict = {
    "name": "Suvojit",
    "age": 22,
    "city": "Kolkata"
}
print(my_dict) # Output: {'name': 'Suvojit', 'age': 22, 'city': 'Kolkata'}

# Accessing values in a dictionary
print(my_dict["name"]) # Output: Suvojit

# Adding a new key-value pair to the dictionary
my_dict["country"] = "India"
print(my_dict) # Output: {'name': 'Suvojit', 'age': 22, 'city': 'Kolkata', 'country': 'India'}

# Updating a value in the dictionary
my_dict["age"] = 23
print(my_dict) # Output: {'name': 'Suvojit', 'age': 23, 'city': 'Kolkata', 'country': 'India'}

# Removing a key-value pair from the dictionary
del my_dict["city"]
print(my_dict) # Output: {'name': 'Suvojit', 'age': 23, 'country': 'India'}

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, value)
# Output:
# name Suvojit
# age 23
# country India

# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name is present in the dictionary")
# Output: Name is present in the dictionary

# Getting the number of key-value pairs in the dictionary
print(len(my_dict)) # Output: 3

# Clearing all key-value pairs from the dictionary
my_dict.clear()
print(my_dict) # Output: {}
