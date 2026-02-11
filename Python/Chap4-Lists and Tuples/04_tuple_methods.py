# Tuple Methods

t = (1,45,342,2.289,True,"Suvo","Raii")
# count() method returns the number of occurrences of a specified value in the tuple
print(t.count(1)) # Output: 1
print(t.count("Suvo")) # Output: 1
print(t.count("NotInTuple")) # Output: 0
# index() method returns the index of the first occurrence of a specified value in the tuple
print(t.index(342)) # Output: 2
print(t.index("Raii")) # Output: 6
# If the specified value is not found in the tuple, index() will raise a ValueError
try:
    print(t.index("NotInTuple"))
except ValueError as e:
    print(e) # Output: tuple.index(x): x not found

print(len(t)) # Output: 7