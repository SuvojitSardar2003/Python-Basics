# Random Access Memory is volatile, which means that it loses its contents when the computer is turned off. To save data permanently, we need to store it on a non-volatile storage device, such as a hard drive or solid-state drive. In Python, we can use files to store data permanently.

# A file is a named location on a storage device that can hold data. We can create, read, write, and delete files using Python's built-in functions.

# To create a file, we can use the open() function with the 'w' mode (write mode). This will create a new file if it doesn't exist or overwrite an existing file.
# Example:
# Create a new file and write some data to it

file = open('example.txt', 'w')
file.write('Hello, World!\n')
file.write('This is a file example.\n')
file.close()

# In this example, we create a file named 'example.txt' and write two lines of text to it. After writing, we close the file to ensure that the data is saved properly.


# To read data from a file, we can use the open() function with the 'r' mode (read mode). This will allow us to read the contents of the file.By default file is in read mode
# Example:
# Read the contents of the file

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

# In this example, we open the 'example.txt' file in read mode, read its contents into a variable called 'content', and print it to the console. Finally, we close the file.


# We can also use the 'a' mode (append mode) to add data to an existing file without overwriting it.
# Example:
# Append data to the existing file

file = open('example.txt', 'a')
file.write('This line is appended to the file.\n')
file.close()

# In this example, we open the 'example.txt' file in append mode and write a new line of text to it. The existing content of the file remains unchanged, and the new line is added at the end. Finally, we close the file.


# It's important to always close a file after you're done working with it to free up system resources and ensure that data is saved properly. You can also use the with statement to automatically handle closing the file for you.
# Example:
# Using with statement to handle file operations

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# In this example, we use the with statement to open the 'example.txt' file in read mode. The with statement ensures that the file is properly closed after the block of code is executed, even if an error occurs. We read the contents of the file and print it to the console.

# Everything we have done so far is called file input and output (I/O). File I/O allows us to read from and write to files, enabling us to store data permanently and retrieve it when needed.

# Anything else you would like to know about file I/O in Python?
# yes, I would like to know how to handle exceptions when working with files in Python.
# When working with files in Python, it's important to handle exceptions that may occur during file operations. This can help prevent your program from crashing and allow you to provide meaningful error messages to the user.
# You can use a try-except block to catch exceptions that may occur when opening, reading, writing, or closing a file. Here's an example of how to handle exceptions when working with files:
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'example.txt' was not found.")