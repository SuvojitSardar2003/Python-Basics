# Dictionary Methods
my_dict = {
    "name": "Suvojit",
    "age": 22,
    "city": "Kolkata"
}

# Get the value of a key using the get() method
print(my_dict.get("name")) # Output: Suvojit

# Get the value of a key that does not exist using the get() method
print(my_dict.get("country")) # Output: None

# Get the value of a key that does not exist using the get() method with a default value
print(my_dict.get("country", "Not Found")) # Output: Not Found

# Remove a key-value pair using the pop() method
print(my_dict.pop("age")) # Output: 22
print(my_dict) # Output: {'name': 'Suvojit', 'city': 'Kolkata'}

# Remove the last key-value pair using the popitem() method
print(my_dict.popitem()) # Output: ('city', 'Kolkata')
print(my_dict) # Output: {'name': 'Suvojit'}

# Update a dictionary with another dictionary using the update() method
my_dict.update({"country": "India", "age": 23})
print(my_dict) # Output: {'name': 'Suvojit', 'country': 'India', 'age': 23}

# Create a new dictionary using the fromkeys() method
new_dict = dict.fromkeys(["name", "age", "city"], "Unknown")
print(new_dict) # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(my_dict.items()) # Output: dict_items([('name', 'Suvojit'), ('country', 'India'), ('age', 23)])

# keys() method returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys()) # Output: dict_keys(['name', 'country', 'age'])

# values() method returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values()) # Output: dict_values(['Suvojit', 'India', 23])

print(my_dict.get("name"))
print(my_dict["name"])
# they are not same
# get() returns None if the key doesn't exist, while [] raises a KeyError if the key doesn't exist.
