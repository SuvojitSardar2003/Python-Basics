# WAP in python to print the contents of directory using the os module.

import os

# Ask user for the directory path
directory = input("Enter the directory path: ")

# Check if the given path is a directory
if os.path.isdir(directory):
    print(f"\nContents of directory '{directory}':\n")
    
    # List all files and folders in the directory
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified path is not a valid directory.")
