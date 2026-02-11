# 6. Create an empty dictionary.Allow 4 friends to enter their favourite language as value ans use key as their names. Assume that the names of the friends are unique. Print the dictionary.

d = {}

for i in range(4):
    name = input("Enter friend's name: ")
    language = input("Enter friend's favourite language: ")
    #d[name] = language
    d.update({name: language})
print(d)

# 7. If the names of 2 friends are same then what will happen? Will the dictionary allow it or not? Try to create such a dictionary and find out.

# If the names of 2 friends are the same, the dictionary will not allow duplicate keys. When you try to add a new entry with the same key, it will overwrite the existing value associated with that key. Therefore, only the last entry for that key will be stored in the dictionary.

# 8. If language of 2 friends are same then what will happen? Will the dictionary allow it or not? Try to create such a dictionary and find out.

# If the language of 2 friends is the same, the dictionary will allow it because values in a dictionary can be duplicated. The keys must be unique, but the values can be the same. Therefore, you can have multiple friends with the same favourite language in the dictionary without any issues.

# 9. Can you change the values inside a list which contained in set S:
#S = {8, 7, 10, "Suvo", [1, 2, 3]}
# No, you cannot change the values inside a list that is contained in a set because sets in Python can only contain immutable (hashable) types. Lists are mutable (not hashable), so they cannot be added to a set. If you try to run the code above, it will raise a TypeError indicating that an unhashable type (list) is being added to the set.
