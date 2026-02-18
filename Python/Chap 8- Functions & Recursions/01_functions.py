# Functions are reusable blocks of code that perform a specific task. They allow us to break down our code into smaller, more manageable pieces, and can be called multiple times throughout our program.

# Here is an example of a simple function that takes no arguments and prints a message:
def greet():
    print("Hello, welcome to learning Python functions!")

# To call the function, we simply use its name followed by parentheses:
greet()
# Output: Hello, welcome to learning Python functions!

# In this example, we defined a function called `greet` that prints a welcome message. We then called the function, which executed the code inside it and printed the message to the console.

# Functions can also take arguments, which are values that we pass to the function when we call it. This allows us to make our functions more flexible and reusable. Here is an example of a function that takes an argument:
def greet(name):
    print(f"Hello, {name}! Welcome to learning Python functions!")

# To call this function, we need to provide a value for the `name` argument:
greet("Alice")
# Output: Hello, Alice! Welcome to learning Python functions!

# In this example, we defined a function called `greet` that takes one argument, `name`. When we call the function, we pass the value "Alice" as the argument, which is then used in the function to print a personalized greeting message.

# how to create a function
def my_function():
    print("This is a simple function.")
# how to call a function
my_function()
# Output: This is a simple function.

# Everything about Functions:
# 1. Function Definition: A function is defined using the `def` keyword, followed by the function name and parentheses. The code block within the function is indented.

# Example:
def add(a, b):
    return a + b

# 2. Function Call: To execute the function, you call it by using its name followed by parentheses. If the function takes arguments, you can pass them inside the parentheses.

# Example:
result = add(5, 3)
print(result)  # Output: 8

# 3. Arguments: Functions can take arguments, which are values that you pass to the function when you call it. These arguments can be used within the function to perform specific tasks.

# Example:
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!

# 4. Return Statement: Functions can return a value using the `return` statement. This allows you to get a result back from the function after it has completed its task.

# Example:
def square(x):
    return x * x
result = square(4)
print(result)  # Output: 16

# 5. Default Arguments: You can provide default values for function arguments. If the caller does not provide a value for that argument, the default value will be used.

# Example:
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

# 6. Variable Scope: Variables defined inside a function are local to that function and cannot be accessed outside of it. However, you can use global variables if needed, but it's generally recommended to avoid them for better code organization and readability.

# Example:
def my_function():
    local_variable = "I am local to this function."
    print(local_variable)
my_function()  # Output: I am local to this function.
# print(local_variable)  # This will raise an error because local_variable is not defined outside the function.
