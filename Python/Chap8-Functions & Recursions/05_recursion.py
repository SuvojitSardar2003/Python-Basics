# Recursion in Python
# A function that calls itself is called a recursive function.

# Example of a recursive function to calculate factorial:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# Example of a recursive function to calculate Fibonacci numbers:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8