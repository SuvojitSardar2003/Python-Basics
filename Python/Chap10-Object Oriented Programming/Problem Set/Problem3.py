# 3. Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?

# No, it does not change the class attribute.
# It creates a new instance attribute that shadows the class attribute for that object only.

class Test:
    a = 5

obj = Test()
print(obj.a) # Prints the class attribute because instance attribute is not present

obj.a = 0 # Instance attribute is set

print(obj.a) # Prints the instance attribute because instance attribute is present

print(Test.a) # Prints the class attribute