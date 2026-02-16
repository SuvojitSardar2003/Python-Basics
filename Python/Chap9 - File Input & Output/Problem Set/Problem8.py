# 8. WAP to make a copy of file "this.txt".

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt","w") as f:
    f.write(content)

# 9. WAP to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes,both files are identical")
else:
    print("No,files are not identical")

# 10. WAP to wipe out the content of a file using python.

with open("this_copy.txt","w") as f:
    f.write("")