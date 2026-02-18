# 6. WAP to calculate the grade of a student from his marks from the following scheme:
# Marks        Grade
# 90-100       Excellent
# 80-89        A
# 70-79        B
# 60-69        C
# 50-59        D
# <50          F

marks = int(input("Enter your marks: "))

if(marks >=90 and marks <=100):
    print("Your grade is: Excellent")
elif(marks >=80 and marks <=89):
    print("Your grade is: A")
elif(marks >=70 and marks <=79):
    print("Your grade is: B")
elif(marks >=60 and marks <=59):
    print("Your grade is: C")
elif(marks >=50 and marks <=59):
    print("Your grade is: D")
else:
    print("Your grade is: F")


# 7. WAP to find out whether a given post is talking about "Python" or not.
post = input("Enter your post: ")
if("Python" in post):
    print("The post is talking about Python.")
else:
    print("The post is not talking about Python.")