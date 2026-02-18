# 3. How do you prevent a python print() function from printing a new line at the end of the output?

# To prevent the print() function from printing a new line at the end of the output, you can use the 'end' parameter and set it to an empty string. By default, the 'end' parameter is set to '\n', which adds a new line after the output. Here's an example:
print("Hello, ", end="")
print("World!")